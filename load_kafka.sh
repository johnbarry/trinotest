cat book.json  | $HOME/kafka_2.13-3.1.0/bin/kafka-console-producer.sh --topic jpb.book  --bootstrap-server localhost:9092
cat bookSale.json  | $HOME/kafka_2.13-3.1.0/bin/kafka-console-producer.sh --topic jpb.bookSale --bootstrap-server localhost:9092
cat *pany.json  | $HOME/kafka_2.13-3.1.0/bin/kafka-console-producer.sh --topic jpb.company --bootstrap-server localhost:9092

