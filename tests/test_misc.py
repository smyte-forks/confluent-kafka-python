#!/usr/bin/env python

import confluent_kafka_smyte


def test_version():
    print('Using confluent_kafka_smyte module version %s (0x%x)' % confluent_kafka_smyte.version())
    sver, iver = confluent_kafka_smyte.version()
    assert len(sver) > 0
    assert iver > 0

    print('Using librdkafka version %s (0x%x)' % confluent_kafka_smyte.libversion())
    sver, iver = confluent_kafka_smyte.libversion()
    assert len(sver) > 0
    assert iver > 0

