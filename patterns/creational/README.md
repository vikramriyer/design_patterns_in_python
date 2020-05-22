## Creational Patterns

### Factory
When we have to decide the object in runtime, we use the factory pattern.
Ex: Suppose we have 2 ml models for classification; RandomForest and NaiveBayes, and we want to decide which model to use based on inputs from API.
In such a case, we can have a Factory Class/Method that can check the keyword and invoke the corresponding class (ml model)
> Corresponding code file: [factory.py](factory.py) in the same directory.

Since the factory class helps us create other objects, it is a creational pattern.

If you need a more comprehensive example, visit this blog.

https://realpython.com/factory-method-python/

### Singleton

### Builder

### Prototype
