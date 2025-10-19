<h1>
Install confluent-kafka dependency
</h1>
```pip3 install confluent-kafka```
<h1>
Validate that the topic was created in kafka container
</h1>
```docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092```
<h1>
Describe that topic and see its partitions
</h1>
```docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic new_orders```
<h1>
View all events in a topic
</h1>
```docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning```
