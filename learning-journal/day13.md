# Day 13

## Date
14 July 2026

## What is a Dataclass?
Dataclass is special pythin construct where object initialization , string conversion and complare like methods (boilerplate code) is by default handled by python.it is used when the respondinilty of the class is just to store data and not having much behavior.

## Why use Dependency Injection?
To externalize the responsibility of other object creations outside of the class instead of assigning supportive objects within the class. It supports #1 SOLID principle of Segregation of responsibility.
It helps in easy usint testing , changing class behaviour at runtime etc.

## Why is logging important?
TO have a formatted application event repository that can be searched, grouped based on criticality and feed to external tools to show in dashboard , reports etc.

## Why avoid hardcoding configuration?
So that the values can be stored at center place and any change in those values can be done only at one place. It avoids risks of missing the replacement of the value cross multiple modules and provide a cleaner verison of code.

## What production improvements did I make today?
Introduced logging, exception handling and configuration driven development 

## Confidence (1–10)
10