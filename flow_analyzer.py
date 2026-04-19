from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()
flow_stats = {}

# Host name mapping
host_map = {
    "00:00:00:00:00:01": "h1",
    "00:00:00:00:00:02": "h2",
    "00:00:00:00:00:03": "h3",
    "00:00:00:00:00:04": "h4"
}

def name(mac):
    return host_map.get(mac.lower(), mac)

def show_table():
    print("\n======= FLOW TABLE ANALYZER =======")
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "Switch", "Source", "Dest", "Packets", "Status"
    ))
    print("-" * 50)

    for key, count in flow_stats.items():
        sw, src, dst = key
        status = "ACTIVE" if count > 0 else "UNUSED"
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(
            "s" + str(sw), name(src), name(dst), count, status
        ))

def _handle_ConnectionUp(event):
    log.info("Switch %s connected", event.dpid)

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet:
        return

    src = str(packet.src).lower()
    dst = str(packet.dst).lower()
    dpid = event.dpid
    key = (dpid, src, dst)

    if key not in flow_stats:
        flow_stats[key] = 0

    flow_stats[key] += 1

    show_table()

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Flow Analyzer Controller Started")
