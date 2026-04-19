# Multi-Switch Flow Table Analyzer

## Problem Statement

This project analyzes traffic flows across multiple OpenFlow switches in a Mininet SDN network using a POX controller.

## Features

* Multi-switch traffic monitoring
* Displays source and destination flows
* Packet count tracking
* Active flow detection
* Real-time controller updates

## Tools Used

* Ubuntu VM
* Mininet
* POX Controller
* Open vSwitch
* Python

## Topology

Linear topology with 3 switches and connected hosts.

## How to Run

### Start Controller

```bash id="z2m6v9"
cd ~/pox
python3 pox.py flow_analyzer
```

### Start Mininet

```bash id="v1r4k7"
sudo mn --controller=remote --topo linear,3
```

### Scenario 1

```bash id="d8q3w1"
pingall
```

### Scenario 2

```bash id="x9m5t2"
h1 iperf -s &
h2 iperf -c h1
```

## Output

* Hosts communicate successfully
* Flow analyzer displays active traffic
* Packet counts update dynamically

## Screenshots

See screenshots folder.

## References

* Mininet Documentation
* POX Documentation
* OpenFlow Concepts
