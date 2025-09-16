#!/usr/bin/env python3
"""
GEE File Monitor
================
Monitors GEE_Outbox for completed files and moves them to project folders

Author: GIS Engineer
Date: 2025-01-23
Version: 1.0
"""

import os
import time
import shutil
from pathlib import Path
from datetime import datetime

class GEEFileMonitor:
    """Monitors GEE_Outbox and manages file movement"""
    
    def __init__(self, config):
        self.config = config
        self.gee_outbox = Path(config['gee_outbox'])
        self.poll_interval = config['poll_interval']
        self.max_wait = config['max_wait']
        self.expected_outputs = config['expected_outputs']
        
    def monitor_and_move_files(self, tasks, project_path, output_dir, property_name):
        """Monitor GEE tasks and move completed files to project folder"""
        
        print(f"\n{'='*60}")
        print("📊 Monitoring export tasks and moving files...")
        print(f"{'='*60}")
        
        start_time = time.time()
        completed_files = []
        
        # Create target directory
        target_dir = output_dir / "woody_masks"
        target_dir.mkdir(exist_ok=True)
        
        while tasks and (time.time() - start_time) < self.max_wait:
            remaining_tasks = []
            
            for name, task, export_name in tasks:
                try:
                    status = task.status()
                    state = status.get('state', 'UNKNOWN')
                    
                    if state == 'COMPLETED':
                        print(f"✅ {name}: COMPLETED - {export_name}")
                        
                        # Look for the file in GEE_Outbox
                        file_moved = self._move_completed_file(
                            export_name, target_dir, property_name
                        )
                        
                        if file_moved:
                            completed_files.append(export_name)
                            print(f"📁 Moved: {export_name}")
                        else:
                            print(f"⚠️  File not found in GEE_Outbox: {export_name}")
                            
                    elif state == 'FAILED':
                        error = status.get('error_message', 'Unknown error')
                        print(f"❌ {name}: FAILED - {error}")
                        
                    else:
                        remaining_tasks.append((name, task, export_name))
                        print(f"⏳ {name}: {state}")
                        
                except Exception as e:
                    print(f"⚠️  {name}: Error checking status - {e}")
                    remaining_tasks.append((name, task, export_name))
            
            tasks = remaining_tasks
            
            if tasks:
                elapsed = time.time() - start_time
                print(f"\n⏰ Elapsed time: {elapsed/60:.1f} minutes")
                print(f"⏳ Waiting {self.poll_interval} seconds before next check...")
                time.sleep(self.poll_interval)
        
        # Check if we have all expected files
        total_time = time.time() - start_time
        print(f"\n🎉 Monitoring complete! Total time: {total_time/60:.1f} minutes")
        print(f"📊 Completed files: {len(completed_files)}/{self.expected_outputs}")
        
        if len(completed_files) == self.expected_outputs:
            print("✅ All expected files completed and moved successfully!")
            return True
        elif len(completed_files) > 0:
            print(f"⚠️  Partial completion: {len(completed_files)}/{self.expected_outputs} files")
            return True
        else:
            print("❌ No files completed")
            return False
    
    def _move_completed_file(self, export_name, target_dir, property_name):
        """Move a completed file from GEE_Outbox to target directory"""
        
        # Look for the file in GEE_Outbox
        # GEE typically creates files with .tif extension
        possible_names = [
            f"{export_name}.tif",
            f"{export_name}.tiff",
            export_name
        ]
        
        # Also check for files that might have different naming patterns
        # GEE sometimes modifies the export name slightly
        for filename in possible_names:
            source_file = self.gee_outbox / filename
            if source_file.exists():
                # Create target filename with proper naming convention
                target_filename = self._create_target_filename(filename, property_name)
                target_file = target_dir / target_filename
                
                try:
                    # Move the file
                    shutil.move(str(source_file), str(target_file))
                    
                    # Verify the move
                    if target_file.exists():
                        print(f"✅ Moved: {filename} → {target_filename}")
                        return True
                    else:
                        print(f"❌ Move failed: {filename}")
                        return False
                        
                except Exception as e:
                    print(f"❌ Error moving {filename}: {e}")
                    return False
        
        # If exact match not found, try to find files that start with the export name
        print(f"🔍 Searching for files starting with: {export_name}")
        for file_path in self.gee_outbox.glob(f"{export_name}*"):
            if file_path.is_file():
                print(f"📁 Found matching file: {file_path.name}")
                try:
                    # Create target filename with proper naming convention
                    target_filename = self._create_target_filename(file_path.name, property_name)
                    target_file = target_dir / target_filename
                    
                    # Move the file
                    shutil.move(str(file_path), str(target_file))
                    
                    # Verify the move
                    if target_file.exists():
                        print(f"✅ Moved: {file_path.name} → {target_filename}")
                        return True
                    else:
                        print(f"❌ Move failed: {file_path.name}")
                        return False
                        
                except Exception as e:
                    print(f"❌ Error moving {file_path.name}: {e}")
                    return False
        
        return False
    
    def _create_target_filename(self, original_filename, property_name):
        """Create properly formatted target filename"""
        
        # Extract base name without extension
        base_name = Path(original_filename).stem
        
        # Ensure proper naming convention: WoodyMethod_FarmName_Date.tif
        # The GEE export should already be in this format, but let's verify
        
        # If it's already properly formatted, use as-is
        if base_name.startswith('Woody') and '_' in base_name:
            return f"{base_name}.tif"
        
        # Otherwise, try to construct it
        farm_name = property_name.replace('_', '')
        timestamp = datetime.now().strftime('%Y%m%d')
        
        # This is a fallback - the GEE export should already be properly named
        return f"WoodyMask_{farm_name}_{timestamp}.tif"
    
    def cleanup_gee_outbox(self, property_name):
        """Clean up any remaining files in GEE_Outbox for this property"""
        
        print(f"\n🧹 Cleaning up GEE_Outbox for {property_name}...")
        
        farm_name = property_name.replace('_', '')
        timestamp = datetime.now().strftime('%Y%m%d')
        
        # Look for files matching this property's pattern
        pattern_files = list(self.gee_outbox.glob(f"Woody*{farm_name}*{timestamp}*"))
        
        for file_path in pattern_files:
            try:
                file_path.unlink()  # Delete the file
                print(f"🗑️  Removed: {file_path.name}")
            except Exception as e:
                print(f"⚠️  Could not remove {file_path.name}: {e}")
        
        print("✅ Cleanup complete")
