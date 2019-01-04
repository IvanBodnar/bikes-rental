#### Usage
- Clone the repository
- Cd into the cloned folder
- Create a virtualenv (python 3.7 used) and activate it
- Execute pip install -r requirements.txt
##### To execute the tests:
- Cd into src
- To execute the tests:
``` bash
$ pytest
```
- To execute coverage:
``` bash
$ pytest --cov=.
```

#### Project Description
This project was implemented trying to achieve the maximum level of decoupling
among classes, through the use of composition over inheritance.  
Inheritance was used, though, in the case of the Promotion class: it made 
sense to enforce an interface in that case, to be used with the Account class.  
In the case of the set of classes representing the rental business object, it made sense
to me to create the different types of rentals as distinct classes composed by a Rental class,
which holds their common functionality. These classes in turn are used to compose a PurchasedRental class,
which is going to be used to represent a concrete rental.
