# Numerical Analysis

<p align="center">
  <img src="https://github.com/VsIG-official/Numerical-Analysis/blob/master/Labs/Additional-Materials/Graph.png" data-canonical-src="https://github.com/VsIG-official/Numerical-Analysis/blob/master/Labs/Additional-Materials/Graph.png" width="500" />
</p>

## Table of Contents

- [Description](#description)
- [Badges](#badges)
- [Contributing](#contributing)
- [License](#license)

### Description

My Labs for Numerical Analysis

## Badges

[![Theme](https://img.shields.io/badge/Theme-Math-blue)](https://img.shields.io/badge/Theme-Math-blue)
[![Language](https://img.shields.io/badge/Language-Python-blue)](https://img.shields.io/badge/Language-Python-blue)

---

## Example

```python
# completion criterion
while epsilonValue < abs(MyFunction(finalNumber)) and epsilonValue < abs(firstInterval - secondInterval):
	# if 0, then do bisection
        if index == 0:
        	finalNumber = (secondInterval + firstInterval) / half
        # else do chords
        else:
                finalNumber = (MyFunction(secondInterval) * firstInterval - MyFunction(firstInterval) * secondInterval) / (MyFunction(secondInterval) - MyFunction(firstInterval))

        if MyFunction(secondInterval) * MyFunction(finalNumber) <= 0:
        	firstInterval = finalNumber
        else:
                secondInterval = finalNumber

        numberOfIterations = numberOfIterations + 1

    	return finalNumber, numberOfIterations

```

---

## Contributing

> To get started...

### Step 1

- 🍴 Fork this repo!

### Step 2

- **HACK AWAY!** 🔨🔨🔨

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2021 © <a href="https://github.com/VsIG-official" target="_blank">VsIG</a>.
