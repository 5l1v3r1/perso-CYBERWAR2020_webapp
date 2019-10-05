# CYBERWAR2020_WebApp
## KICK OFF
Développer une application web pour guider les joueurs, indiquer les règles des cartes et récolter les données du jeu pendant les soirées test.

## TECHNOLOGIES
- Server: [Django 2.2.6](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
- HTTP Server embded to Django (API available)
- default DB embded to Django: [SQLite](https://sqlite.org/index.html)
- Server side language (except if embded in Django?): [Node.js](https://www.hongkiat.com/blog/node-js-server-side-javascript/)

## IMPORTANT UPDATES
* CHECK README.md before developping!!


* Django server in dir 'Web' parametrized and ready to use! PULL GIT ASAP (ask Ben for more info)

## [OUTLINE](https://gitlab.montefiore.ulg.ac.be/Benjamin/cyberwar2020_webapp/blob/master/PDF/Outline.pdf)

* Pages skeleton: [sketch of pages skeleton](https://gitlab.montefiore.ulg.ac.be/Benjamin/cyberwar2020_webapp/blob/master/PDF/sketchPagesSkeleton.pdf)

* Pages design (Ben)

* App Server: games saloon, DB buffers (Thib)

* DB design (Ben): [sketch of DB tables](https://gitlab.montefiore.ulg.ac.be/Benjamin/cyberwar2020_webapp/blob/master/PDF/sketchTableDB.pdf)

* DB gestion (Quentin, Ben)

* DB/App server communication (->QUENTIN/THIB)

* Deployment and users connection (solved?)

## ISSUES

### GENERAL

* Quelle SGBD utiliser? SQLite? pas limité accès depuis DB buffer? (->QUENTIN/THIB)  
/!/ server django default DBGS is SQLite (seems good to me - Ben) (to close)

### Benjamin

* Multiple entry with same name if refreshing from 'confirmnewid' page. Should redirect to 'Connected'. (Ben)

* Create session for a user to connect and save ID, NAME, FIRSTNAME (Ben)

### Quentin

### Thibault

### Thomas
