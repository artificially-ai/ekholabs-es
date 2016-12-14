# What's the goal?

The goal here is to share some knowledge about Elasticsearch and how to use it with Python 2.7.

# What is being used?

In this sample project we use the following aspects of Elasticsearch:

* Settings
* Mappings
* Indexes
* Documents
* Queries

# How is it deployed?

The current implementation depends on AWS when it comes to the Elasticsearch server. So, in order to move forward, you are expected to have access to a AWS ES domain.

There might be other deployment options in the future. But if it takes too long, do not hesite to fork, fix, and send a PR towards this repository.

# How do I talk to the AWS ES domain?

The project offers a RESTful API implementation that can be used for the following purposes:

* Create indexes
* Create documents
* Query indexes
* Delete documents
* Delete indexes

# Dependencies

In order to run it, you will need to install the following:

* Python 2.7
* Pip
* elasticsearch
* requests-aws4auth
* web.py

Just use Pip for the last 3 libraries on the list above.

# Running the project

After cloning the project, please edit the file ```config/properties.json``` in order to configure the AWS connection.

Once that's done, you do the following to run the project:

```
python webserver.py
```

# How can I test the API calls listed above?

The best way to test the APIs is using Postman. Have a look at the ```webserver.py``` to understand how to call the endpoints. In addition, under the resources directory, you can find sample files for the following:

* Mapping
* Documents
* Query

**Have fun!**
