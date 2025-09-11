---
title: Correlation Between Two Risk Inputs
version: 2016
category: Risk Analysis
original_file: 65_Correlation Between Two Risk Inputs_2016.md
---

[Risk Properties of an
Input window : *Edit
Correlation* button]

Enter the correlation between two risk inputs.

**Use**

Enter a number from --1.0 to +1.0.

A value of 0.0 indicates that the two risk inputs are not correlated:
when one rises, the other is just as likely to fall as to rise.
Uncorrelated inputs are not necessarily independent (they can be related
in a non-linear way, such as x and y in x = y * y).

A value of +1.0 indicates that the risk inputs are fully positively
linearly correlated: whenever one increases by a certain amount, the
other increases by a proportional amount.

A value of --1.0 indicates that the risk inputs are fully negatively
linearly correlated: whenever one increases by a certain amount, the
other decreases by a proportional amount.

A value between 0.0 and +1.0 indicates that the risk inputs are somewhat
positively linearly correlated: when one increases by a certain amount,
the other is more likely to rise than to fall, and tends to do so by a
proportional amount.

A value between 0.0 and --1.0 indicates that the risk inputs are
somewhat negatively linearly correlated: when one increases by a certain
amount, the other is more likely to fall than to rise, and tends to do
so by a proportional amount.