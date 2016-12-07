# -*- coding: utf-8 -*-
from troposphere import GetAtt, Output, Ref
from troposphere.sqs import Queue


from .template import template


mysourcequeue = template.add_resource(Queue(
    "DashboardQueue",
))

template.add_output([
    Output(
        "DashboardQueueURL",
        Description="URL of the source queue",
        Value=Ref(mysourcequeue)
    ),
    Output(
        "DashboardQueueARN",
        Description="ARN of the source queue",
        Value=GetAtt(mysourcequeue, "Arn")
    )
])
