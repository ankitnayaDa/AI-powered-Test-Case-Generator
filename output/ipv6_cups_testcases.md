```json
{
  "feature": "IPv6 support in 4G CUPS",
  "system": "4G LTE EPC - CUPS Architecture",
  "test_cases": [
    {
      "id": "CUPS_IPV6_TC_001",
      "category": "Functional",
      "description": "Validate IPv6 session establishment with SGW-U and PGW-U",
      "preconditions": [
        "SGW-C and PGW-C microservices are running and healthy in Kubernetes",
        "UPF (SGW-U/PGW-U) instances are running and associated with CP",
        "UE is configured to request an IPv6 address",
        "PFCP association is established between SGW-C and UPF, and PGW-C and UPF",
        "Network infrastructure (e.g., routers) supports IPv6 routing between UPF and external network"
      ],
      "steps": [
        "Initiate PDN session creation request from a UE requesting IPv6 connectivity",
        "Monitor PFCP messages for session establishment requests containing IPv6 context (e.g., requested IP type)",
        "Verify UPF allocates an IPv6 address to the UE",
        "Verify PFCP session modification messages update the session with IPv6 address information",
        "Send IPv6 traffic from the UE towards the external IPv6 network",
        "Verify UPF forwards IPv6 traffic correctly, utilizing S5/S8 for control and Gi/SGi for user plane"
      ],
      "expected_result": "An IPv6-only PDN session is successfully established for the UE. IPv6 traffic flows bidirectionally between the UE and the external IPv6 network without loss or distortion.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_002",
      "category": "Functional",
      "description": "Validate Dual-Stack (IPv4/IPv6) session establishment with SGW-U and PGW-U",
      "preconditions": [
        "SGW-C and PGW-C microservices are running and healthy",
        "UPF (SGW-U/PGW-U) instances are running and associated with CP",
        "UE is configured to request both IPv4 and IPv6 addresses",
        "PFCP association is established",
        "Network infrastructure supports IPv4 and IPv6 routing"
      ],
      "steps": [
        "Initiate PDN session creation request from a UE requesting dual-stack connectivity",
        "Monitor PFCP messages for session establishment requests indicating dual-stack support",
        "Verify UPF allocates both an IPv4 and an IPv6 address to the UE",
        "Verify PFCP session modification messages update the session with both IPv4 and IPv6 address information",
        "Send IPv4 traffic from the UE",
        "Send IPv6 traffic from the UE",
        "Verify UPF correctly handles and routes both IPv4 and IPv6 traffic streams"
      ],
      "expected_result": "A dual-stack PDN session is successfully established. Both IPv4 and IPv6 traffic flow bidirectionally between the UE and the respective external networks.",
      "protocol": ["PFCP", "GTP-U", "IPv4", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_003",
      "category": "Functional",
      "description": "Validate PFCP session establishment with IPv6 parameters and specific QoS",
      "preconditions": [
        "SGW-C and PGW-C are running",
        "UPF instances are running and associated",
        "UE supports IPv6 and specific QoS requirements",
        "PFCP association is established",
        "QoS profiles for IPv6 traffic are configured on the network elements"
      ],
      "steps": [
        "Initiate PDN session creation request from UE with IPv6 and specified QoS parameters",
        "Observe PFCP 'Session Establishment Request' messages, ensuring IPv6 address family and QoS IE are correctly populated",
        "Verify UPF creates a QoS flow for the IPv6 session based on the requested parameters",
        "Confirm PFCP 'Session Establishment Response' confirms session setup with correct IPv6 details and QoS"
      ],
      "expected_result": "PFCP session is established with correct IPv6 address family and QoS parameters. The UPF correctly enforces the specified QoS for IPv6 traffic.",
      "protocol": ["PFCP", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_004",
      "category": "Functional",
      "description": "Validate IPv6 address allocation mechanisms (DHCPv6/SLAAC)",
      "preconditions": [
        "SGW-C and PGW-C are running",
        "UPF instances are running and configured to support IPv6 address assignment methods",
        "PFCP association is established",
        "External IPv6 network is configured for address delegation (if applicable)"
      ],
      "steps": [
        "Configure UPF to use DHCPv6 for IPv6 address assignment",
        "Initiate session setup for an IPv6 UE",
        "Monitor UPF's interaction with DHCPv6 server (if external)",
        "Verify UPF assigns an IPv6 address to the UE",
        "Configure UPF to use SLAAC for IPv6 address assignment",
        "Initiate session setup for an IPv6 UE",
        "Verify UPF facilitates SLAAC process and assigns an IPv6 address to the UE"
      ],
      "expected_result": "The UPF successfully allocates IPv6 addresses to UEs using the configured method (DHCPv6 or SLAAC).",
      "protocol": ["PFCP", "IPv6", "DHCPv6", "SLAAC"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_005",
      "category": "Functional",
      "description": "Validate Control and User Plane Separation (CUPS) for IPv6 traffic",
      "preconditions": [
        "SGW-C and PGW-C are operational",
        "SGW-U and PGW-U (UPF) instances are operational and distinct",
        "PFCP association is established",
        "UE connected with an IPv6 session"
      ],
      "steps": [
        "Initiate IPv6 traffic flow from UE",
        "Monitor control plane traffic (PFCP, S5/S8 control) during session setup/modification",
        "Monitor user plane traffic (GTP-U, S5/S8 user, Gi/SGi) carrying IPv6 packets",
        "Induce a temporary outage or high load on SGW-C/PGW-C and observe impact on user plane forwarding of IPv6 traffic",
        "Induce a temporary outage or high load on SGW-U/PGW-U and observe impact on control plane signaling for IPv6 sessions"
      ],
      "expected_result": "Control plane signaling for IPv6 sessions operates independently of user plane traffic forwarding. Changes in control plane state do not disrupt active IPv6 user plane traffic and vice-versa, demonstrating true CUPS.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_006",
      "category": "Functional",
      "description": "Validate IPv6 session lifecycle: Create, Modify, Delete",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running and healthy",
        "PFCP association is established",
        "UE connected with an IPv6 session"
      ],
      "steps": [
        "Create an IPv6 session for a UE",
        "Verify session establishment and IPv6 address assignment",
        "Modify the IPv6 session (e.g., change QoS, add/remove PDU sessions within the same bearer)",
        "Verify PFCP 'Session Modification Request' and 'Response' messages",
        "Verify UPF updates session parameters accordingly",
        "Delete the IPv6 session",
        "Verify PFCP 'Session Deletion Request' and 'Response' messages",
        "Confirm UE loses IPv6 connectivity"
      ],
      "expected_result": "IPv6 sessions can be reliably created, modified, and deleted through PFCP signaling. Session state is consistently maintained across control and user planes.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_007",
      "category": "Failover & Recovery",
      "description": "Validate SGW-C/PGW-C failover and recovery with active IPv6 sessions",
      "preconditions": [
        "SGW-C and PGW-C are deployed in a high-availability configuration (e.g., multiple replicas)",
        "UPF instances are running and associated with active CP instances",
        "Multiple UEs are connected with active IPv6 sessions",
        "PFCP associations are healthy"
      ],
      "steps": [
        "Gracefully restart one instance of SGW-C",
        "Monitor PFCP re-association and session recovery",
        "Verify active IPv6 sessions remain active with minimal disruption (e.g., brief packet loss)",
        "Send new IPv6 session establishment requests during SGW-C restart",
        "Repeat steps for PGW-C",
        "Simulate unhealthy state for SGW-C/PGW-C pods (e.g., network partition, resource exhaustion) and verify auto-healing/failover"
      ],
      "expected_result": "Upon SGW-C or PGW-C failure and recovery, existing IPv6 sessions are seamlessly re-established with minimal service interruption. New session establishment during failure is handled correctly by the surviving CP instance.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_008",
      "category": "Failover & Recovery",
      "description": "Validate UPF (SGW-U/PGW-U) restart and recovery with active IPv6 sessions",
      "preconditions": [
        "SGW-C and PGW-C are running",
        "UPF instances are running in a multi-instance setup",
        "Multiple UEs are connected with active IPv6 sessions",
        "PFCP associations are healthy"
      ],
      "steps": [
        "Gracefully restart one instance of a UPF (SGW-U or PGW-U)",
        "Monitor PFCP messages for re-association with the CP",
        "Verify active IPv6 sessions are migrated or resumed on a healthy UPF instance",
        "Send IPv6 traffic during UPF restart and observe re-routing and recovery",
        "Simulate unhealthy state for UPF pods and verify rescheduling/re-creation"
      ],
      "expected_result": "Upon UPF failure and recovery, active IPv6 sessions are either maintained through redundancy or quickly resumed on a healthy UPF instance, with minimal impact on traffic flow.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_009",
      "category": "Performance & Scale",
      "description": "Validate performance and scale of IPv6 traffic handling under load",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are deployed and scaled appropriately",
        "PFCP associations are established",
        "Test tools capable of generating high volumes of IPv6 traffic are available"
      ],
      "steps": [
        "Configure test UEs to establish IPv6 sessions",
        "Generate a high volume of sustained IPv6 user plane traffic",
        "Monitor UPF throughput, latency, and resource utilization (CPU, memory)",
        "Monitor SGW-C and PGW-C signaling load (PFCP messages per second)",
        "Gradually increase the number of concurrent IPv6 sessions and traffic load up to system limits",
        "Observe system behavior for any performance degradation, packet drops, or control plane instability"
      ],
      "expected_result": "The system handles a high volume of IPv6 traffic and a large number of concurrent IPv6 sessions without significant performance degradation, packet loss, or control plane instability, meeting defined performance benchmarks.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_010",
      "category": "Interoperability",
      "description": "Interoperability with IPv4-only UEs",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "Network supports both IPv4 and IPv6 traffic",
        "An IPv6-enabled session for another UE is active"
      ],
      "steps": [
        "Connect an IPv4-only UE to the network",
        "Initiate an IPv4 PDN session creation request",
        "Verify the UE receives an IPv4 address",
        "Send IPv4 traffic from the UE",
        "Verify UPF correctly routes IPv4 traffic for this UE",
        "Verify the presence of the IPv4-only UE does not impact the active IPv6 session's performance or stability"
      ],
      "expected_result": "The system correctly handles IPv4-only UEs alongside IPv6-enabled UEs. IPv4 traffic from IPv4-only UEs is routed correctly, and there is no negative impact on existing IPv6 sessions.",
      "protocol": ["PFCP", "GTP-U", "IPv4", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_011",
      "category": "Interoperability",
      "description": "Interoperability with Dual-Stack UEs (mixed traffic types)",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "Network supports both IPv4 and IPv6 traffic"
      ],
      "steps": [
        "Connect a dual-stack UE to the network",
        "Initiate a dual-stack PDN session creation request",
        "Verify the UE receives both IPv4 and IPv6 addresses",
        "Send IPv4 traffic from the UE",
        "Send IPv6 traffic from the UE",
        "Verify UPF correctly routes both IPv4 and IPv6 traffic streams for this UE",
        "Verify the dual-stack UE's traffic does not negatively impact other IPv4-only or IPv6-only sessions"
      ],
      "expected_result": "The system correctly handles dual-stack UEs, managing both IPv4 and IPv6 traffic streams independently and concurrently without interference.",
      "protocol": ["PFCP", "GTP-U", "IPv4", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_012",
      "category": "Security",
      "description": "Validate IPv6 address spoofing prevention",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE connected with an IPv6 session"
      ],
      "steps": [
        "Attempt to send IPv6 packets from a source IP address that is not assigned to the UE or is outside its allocated prefix",
        "Monitor UPF for packet drops or rejection of spoofed packets",
        "Verify UPF does not forward spoofed IPv6 traffic"
      ],
      "expected_result": "The UPF effectively filters out or drops IPv6 packets originating from spoofed source IP addresses, preventing unauthorized network access.",
      "protocol": ["IPv6", "PFCP"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_013",
      "category": "Security",
      "description": "Validate IPv6 traffic filtering and policy enforcement",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE connected with an IPv6 session",
        "Specific IPv6 filtering policies are configured (e.g., block certain IPv6 addresses or ports)"
      ],
      "steps": [
        "Configure policies on PGW-C/UPF to block specific IPv6 destinations or protocols",
        "Attempt to send IPv6 traffic from the UE to a blocked destination/protocol",
        "Verify that the UPF blocks and discards this traffic",
        "Attempt to send IPv6 traffic to an allowed destination/protocol",
        "Verify that this traffic is allowed to pass through"
      ],
      "expected_result": "The system correctly enforces configured IPv6 traffic filtering policies, allowing legitimate traffic and blocking unauthorized traffic based on defined rules.",
      "protocol": ["IPv6", "PFCP"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_014",
      "category": "Network Conditions",
      "description": "IPv6 session handling under packet loss",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE connected with an active IPv6 session"
      ],
      "steps": [
        "Introduce controlled packet loss on the user plane interface (e.g., Gi/SGi or S5/S8 user plane)",
        "Send sustained IPv6 traffic from the UE",
        "Monitor for session re-establishment, traffic retransmissions, and overall session stability",
        "Observe control plane signaling (PFCP) for any impact or retransmissions due to packet loss"
      ],
      "expected_result": "The system maintains IPv6 session stability and data flow integrity even with moderate packet loss. TCP retransmissions for IPv6 traffic are handled, and the session remains up.",
      "protocol": ["IPv6", "PFCP", "GTP-U"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_015",
      "category": "Network Conditions",
      "description": "IPv6 session handling under high latency",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE connected with an active IPv6 session"
      ],
      "steps": [
        "Introduce controlled high latency on the user plane interface (e.g., Gi/SGi or S5/S8 user plane)",
        "Send sustained IPv6 traffic from the UE",
        "Monitor session responsiveness and latency for IPv6 application traffic",
        "Observe control plane signaling (PFCP) for any delays or timeouts"
      ],
      "expected_result": "The system handles IPv6 sessions under high latency conditions. While application performance may be affected, session integrity is maintained, and control plane operations complete within acceptable thresholds.",
      "protocol": ["IPv6", "PFCP", "GTP-U"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_016",
      "category": "Network Conditions",
      "description": "IPv6 session continuity during UPF restart (simulated)",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE connected with an active IPv6 session, sending continuous traffic"
      ],
      "steps": [
        "Initiate a restart of a UPF instance while an IPv6 session is active and transmitting data",
        "Observe the UPF restarting and re-associating with the control plane",
        "Monitor the IPv6 traffic flow during the UPF restart period",
        "Verify that the session resumes and traffic flows again once the UPF is operational"
      ],
      "expected_result": "During a UPF restart, there might be a brief interruption in IPv6 traffic. However, the session should automatically recover and resume data flow once the UPF is back online and re-associated with the control plane.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_017",
      "category": "Network Conditions",
      "description": "IPv6 session continuity during Control Plane restart (simulated)",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE connected with an active IPv6 session, sending continuous traffic"
      ],
      "steps": [
        "Initiate a restart of an SGW-C or PGW-C instance while an IPv6 session is active",
        "Observe the control plane instance restarting and re-associating with UPFs",
        "Monitor the IPv6 traffic flow during the control plane restart period",
        "Verify that the session remains active or quickly recovers once the control plane instance is operational"
      ],
      "expected_result": "During a Control Plane restart, active IPv6 user plane traffic may experience brief disruption but should recover quickly once the control plane instance is back online and re-established associations.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_018",
      "category": "Functional",
      "description": "Validate IPv6 extension headers handling",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE configured to send IPv6 packets with various extension headers (e.g., Hop-by-Hop options, Routing, Fragment, Destination Options)"
      ],
      "steps": [
        "Configure UE to send IPv6 traffic with different types of extension headers",
        "Verify UPF correctly processes and forwards packets with valid extension headers",
        "Attempt to send IPv6 packets with malformed or invalid extension headers",
        "Verify UPF drops or rejects malformed extension headers according to RFC standards"
      ],
      "expected_result": "The UPF correctly handles standard IPv6 extension headers and rejects or drops packets with malformed or invalid extension headers.",
      "protocol": ["IPv6", "PFCP"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_019",
      "category": "Functional",
      "description": "Validate IPv6 Neighbor Discovery Protocol (NDP) functionality",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UE is connected with an IPv6 session and requires NDP for local network communication"
      ],
      "steps": [
        "Initiate communication from UE to another device on the same IPv6 subnet",
        "Verify UE performs Neighbor Solicitation",
        "Verify UPF facilitates the Neighbor Advertisement process (if applicable at UPF layer)",
        "Confirm successful Neighbor Unreachability Detection (NUD)"
      ],
      "expected_result": "The UPF and associated network elements correctly support IPv6 Neighbor Discovery Protocol, allowing UEs to resolve IPv6 addresses to MAC addresses within their local link.",
      "protocol": ["IPv6", "NDP", "PFCP"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_020",
      "category": "Functional",
      "description": "Validate IPv6 Router Advertisements (RA) and Stateless Address Autoconfiguration (SLAAC)",
      "preconditions": [
        "SGW-C, PGW-C, and UPF instances are running",
        "PFCP association is established",
        "UPF is configured to act as an IPv6 router or relay for RAs"
      ],
      "steps": [
        "Configure UPF to send IPv6 Router Advertisements to the UE's subnet",
        "Initiate session setup for an IPv6 UE",
        "Verify the UE receives Router Advertisements",
        "Verify the UE can use RAs to configure its IPv6 address (SLAAC) and discover default gateway"
      ],
      "expected_result": "The UPF correctly provides IPv6 Router Advertisements, enabling UEs to perform stateless address autoconfiguration and establish proper routing for IPv6 connectivity.",
      "protocol": ["IPv6", "RA", "SLAAC", "PFCP"],
      "priority": "Medium"
    }
  ]
}
```