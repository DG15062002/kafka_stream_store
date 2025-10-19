<h2>
Install confluent-kafka dependency
</h2>

```pip3 install confluent-kafka```
<h2>
Validate that the topic was created in kafka container
</h2>

```docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092```
<h2>
Describe that topic and see its partitions
</h2>

```docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic new_orders```
<h2>
View all events in a topic
</h2>

```docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning```
