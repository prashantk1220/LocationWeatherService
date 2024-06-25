**Assumptions**

* Kafka streams the data in the json format with the given data.
* The weather API can be used from a python-library as well for simplicity. 
* Instead of creating a SQL `User` table with all relevant information, just using dictionary here.

---

**Getting Started**

* Run cmd: `make all` in the Terminal. This should create the Kafka Broker service and start the FastAPI service, as mentioned in the Makefile.
* Open the browser and hit the url: https://0.0.0.0:8080/. This will open the Swagger documentation.
* Or directly use the GET endpoint: https://0.0.0.0:8080/users/{user-id} For demo, user-id can be 81325.

---

**Next Steps**

* The error handling can be improved for various cases, instead of just one error-code 404, currently. 
* The user-data along with location and weather can be stored and fetched from DB.
* A better more-accurate weather-service provider can be chosen depending upon the need. 

---

**Resources**

* I googled for free weather services API. Found few opensource with minimal usage and also some available with python-library.
* Created the docker-compose file for Kafka with help of ChatGPT. But it had too many issues to be fixed which consumed most of my time, like Network settings.
  