# Arithmetic Operations Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 22/04/2019
Time            : 20:13
Description     : This is an executable specification file
</pre>


    
## Add integer values in data stores and save it in a new data store
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |val1          |14                |
   |Scenario      |val2          |10                |
   |Scenario      |val3          |12                |

* Add the integer values in data stores and save it in a "Scenario" type data store named "totalVal"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |

* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal     |36            |



## Subtract integer values in data stores and save it in a new data store
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |val1          |14                |
   |Scenario      |val2          |10                |
   |Scenario      |val3          |12                |

* Add the integer values in data stores and save it in a "Scenario" type data store named "val4"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |

* Subtract the integer values in data stores and save it in a "Scenario" type data store named "totalVal2"

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|
   |--------------------|-------------------|---------------------|--------------------|
   |Scenario            |val2               |Scenario             |val4                |

* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal2    |-26           |



## Divide integer values in data stores and save it in a new data store
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |val1          |14                |
   |Scenario      |val2          |10                |
   |Scenario      |val3          |12                |

* Divide the integer values in data stores and save it in a "Scenario" type data store named "totalVal3"

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|
   |--------------------|-------------------|---------------------|--------------------|
   |Scenario            |val1               |Scenario             |val2                |

* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal3    |1.4           |



## Multiply integer values in data stores and save it in a new data store
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |val1          |14                |
   |Scenario      |val2          |10                |
   |Scenario      |val3          |12                |

* Multiply the integer values in data stores and save it in a "Scenario" type data store named "totalVal4"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |

* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal4    |1680          |