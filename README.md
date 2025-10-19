<h2> 
Commands to run the kafka-project 
</h2>

<h3>
Install confluent-kafka dependency
</h3>

```pip3 install confluent-kafka```
<h3>
Validate that the topic was created in kafka container
</h3>

```docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092```
<h3>
Describe that topic and see its partitions
</h3>

```docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic new_orders```
<h3>
View all events in a topic
</h3>

```docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning```
