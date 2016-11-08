#!/usr/bin/env python

import confluent_kafka_smyte

def test_enums():
    """ Make sure librdkafka error enums are reachable directly from the
        KafkaError class without an instantiated object. """
    print(confluent_kafka_smyte.KafkaError._NO_OFFSET)
    print(confluent_kafka_smyte.KafkaError.REBALANCE_IN_PROGRESS)
