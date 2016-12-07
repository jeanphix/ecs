# -*- coding: utf-8 -*-
from stack import (
    domain,
    certificates,
    vpc,
    database,
    assets,
    cluster,
    repository,
    sqs,
    cluster,
)

if __name__ == '__main__':
    print(cluster.template.to_json())
