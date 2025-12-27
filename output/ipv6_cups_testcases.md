```json
{
  "feature": "IPv6 support in 4G CUPS",
  "system": "4G LTE EPC - CUPS Architecture",
  "test_cases": [
    {
      "id": "CUPS_IPV6_TC_001",
      "category": "Functional",
      "description": "Validate IPv6-only session establishment for a UE",
      "preconditions": [
        "SGW-C and PGW-C instances are running and healthy",
        "SGW-U and PGW-U instances are running and healthy",
        "PFCP associations between SGW-C/PGW-C and SGW-U/PGW-U are established",
        "UE is configured to request an IPv6 address",
        "Network elements have IPv6 connectivity enabled"
      ],
      "steps": [
        "Initiate a PDN connection request from an IPv6-capable UE",
        "Monitor PFCP messages for session establishment requests (e.g., 'Create Session Request')",
        "Verify that SGW-C and PGW-C exchange PFCP messages containing IPv6 address pool information",
        "Verify that an IPv6 address is allocated to the UE by the PGW-C (and potentially SGW-C)",
        "Verify PFCP session modification messages confirm the presence of IPv6 bearer context",
        "Send IPv6 traffic (e.g., ping, HTTP request) from the UE to an IPv6-enabled destination",
        "Monitor traffic flow through SGW-U and PGW-U using their respective interfaces (S5/S8-U, Gi/SGi)",
        "Verify successful reception of IPv6 traffic at the destination"
      ],
      "expected_result": "An IPv6-only PDN session is successfully established, and IPv6 traffic flows bi-directionally between the UE and the destination.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_002",
      "category": "Functional",
      "description": "Validate dual-stack (IPv4/IPv6) session establishment for a UE",
      "preconditions": [
        "SGW-C and PGW-C instances are running and healthy",
        "SGW-U and PGW-U instances are running and healthy",
        "PFCP associations between SGW-C/PGW-C and SGW-U/PGW-U are established",
        "UE is configured to request both IPv4 and IPv6 addresses",
        "Network elements have dual-stack (IPv4/IPv6) capabilities enabled"
      ],
      "steps": [
        "Initiate a PDN connection request from a dual-stack capable UE",
        "Monitor PFCP messages for session establishment requests",
        "Verify that SGW-C and PGW-C exchange PFCP messages indicating dual-stack session establishment",
        "Verify that both an IPv4 and an IPv6 address are allocated to the UE",
        "Verify PFCP session modification messages confirm the presence of both IPv4 and IPv6 bearer contexts",
        "Send IPv4 traffic from the UE to an IPv4-enabled destination",
        "Send IPv6 traffic from the UE to an IPv6-enabled destination",
        "Monitor traffic flow through SGW-U and PGW-U",
        "Verify successful reception of both IPv4 and IPv6 traffic at their respective destinations"
      ],
      "expected_result": "A dual-stack PDN session is successfully established, and both IPv4 and IPv6 traffic flows bi-directionally between the UE and destinations.",
      "protocol": ["PFCP", "GTP-U", "IPv4", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_003",
      "category": "Functional",
      "description": "Validate IPv6 address allocation and routing via SGW-C/PGW-C",
      "preconditions": [
        "SGW-C and PGW-C instances are running and healthy",
        "IPv6 address pools are configured on PGW-C",
        "Routing policies for IPv6 are configured on PGW-C and network infrastructure"
      ],
      "steps": [
        "Initiate multiple PDN connection requests for IPv6 sessions",
        "Observe the IPv6 addresses assigned to each UE",
        "Verify that the assigned IPv6 addresses are within the configured pools",
        "Verify that each UE receives a unique IPv6 address",
        "Trace the routing path for outgoing IPv6 traffic from the UE to an external IPv6 network",
        "Verify that the traffic is correctly routed through SGW-U, PGW-U, and the egress gateway"
      ],
      "expected_result": "IPv6 addresses are allocated correctly from configured pools, and IPv6 traffic is routed effectively through the network.",
      "protocol": ["PFCP", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_004",
      "category": "Control Plane",
      "description": "Validate PFCP session establishment with specific IPv6 parameters",
      "preconditions": [
        "SGW-C and PGW-C instances are running and healthy",
        "PFCP association is established"
      ],
      "steps": [
        "Trigger a 'Create Session Request' PFCP message from SGW-C to PGW-C",
        "Include IPv6-specific Information Elements (IEs) in the request, such as IPv6 address prefix delegation or specific address assignment requests",
        "Observe the 'Create Session Response' from PGW-C",
        "Verify that the response correctly reflects the IPv6 parameters requested or allocated",
        "If applicable, trigger a 'Modify Session Request' with IPv6 parameter changes",
        "Verify the corresponding 'Modify Session Response'"
      ],
      "expected_result": "PGW-C correctly processes PFCP messages containing IPv6 parameters, and session state is updated accordingly.",
      "protocol": ["PFCP", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_005",
      "category": "Control Plane",
      "description": "Validate Control and User Plane Separation (CUPS) for IPv6 traffic",
      "preconditions": [
        "SGW-C/PGW-C and SGW-U/PGW-U are deployed as separate microservices",
        "PFCP communication is established between control and user plane components",
        "UE has an established IPv6 session"
      ],
      "steps": [
        "Send IPv6 traffic from the UE",
        "Monitor the flow of signaling (PFCP) between SGW-C and SGW-U, and PGW-C and PGW-U",
        "Independently monitor the flow of user data (GTP-U/GTP-C encapsulation) between SGW-U and PGW-U",
        "Simulate a failure or restart on SGW-C while SGW-U is operational",
        "Verify that user plane traffic continues to flow or recovers seamlessly",
        "Simulate a failure or restart on SGW-U while SGW-C is operational",
        "Verify that session state can be restored on the new SGW-U instance by SGW-C"
      ],
      "expected_result": "Control plane functions (session management) are isolated from user plane functions (data forwarding), and each can be managed or restarted independently without interrupting ongoing IPv6 data flows.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_006",
      "category": "Session Lifecycle",
      "description": "Validate IPv6 session creation, modification, and deletion",
      "preconditions": [
        "SGW-C/PGW-C and SGW-U/PGW-U are running",
        "UE is capable of IPv6 connectivity"
      ],
      "steps": [
        "Create an IPv6-only PDN session",
        "Verify session establishment and IPv6 address assignment",
        "Modify the IPv6 session to add/remove QoS or change bearer parameters",
        "Verify that PFCP messages reflect the modifications and the session state is updated",
        "Delete the IPv6 session",
        "Verify that PFCP messages indicate session deletion",
        "Verify that the UE loses IPv6 connectivity and the allocated IPv6 address is released"
      ],
      "expected_result": "IPv6 sessions can be reliably created, modified with various parameters, and cleanly deleted, maintaining session integrity throughout the lifecycle.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_007",
      "category": "Failover/Recovery",
      "description": "Validate SGW-C failover and recovery with active IPv6 sessions",
      "preconditions": [
        "SGW-C is deployed in a HA configuration (e.g., active-standby or clustered)",
        "Multiple IPv6 sessions are active",
        "SGW-U is operational and connected to the active SGW-C"
      ],
      "steps": [
        "Trigger a failure in the active SGW-C instance (e.g., simulate pod crash)",
        "Monitor the transition to the standby/new SGW-C instance",
        "Verify that the new SGW-C establishes PFCP associations with SGW-U",
        "Verify that existing IPv6 sessions are restored and continue to function",
        "Send IPv6 traffic from UEs after failover",
        "Verify successful traffic flow"
      ],
      "expected_result": "Upon SGW-C failure, a new instance takes over, re-establishes PFCP associations, and restores active IPv6 sessions with minimal interruption.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_008",
      "category": "Failover/Recovery",
      "description": "Validate PGW-C failover and recovery with active IPv6 sessions",
      "preconditions": [
        "PGW-C is deployed in a HA configuration",
        "Multiple IPv6 sessions are active",
        "PGW-U is operational and connected to the active PGW-C"
      ],
      "steps": [
        "Trigger a failure in the active PGW-C instance",
        "Monitor the transition to the standby/new PGW-C instance",
        "Verify that the new PGW-C establishes PFCP associations with PGW-U",
        "Verify that existing IPv6 sessions are restored and continue to function",
        "Send IPv6 traffic from UEs after failover",
        "Verify successful traffic flow"
      ],
      "expected_result": "Upon PGW-C failure, a new instance takes over, re-establishes PFCP associations, and restores active IPv6 sessions with minimal interruption.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_009",
      "category": "Failover/Recovery",
      "description": "Validate UPF (SGW-U/PGW-U) restart and recovery with active IPv6 sessions",
      "preconditions": [
        "SGW-U and PGW-U are deployed in a HA configuration or support graceful restart",
        "Multiple IPv6 sessions are active",
        "SGW-C and PGW-C are operational"
      ],
      "steps": [
        "Gracefully restart an SGW-U instance",
        "Monitor PFCP messages between SGW-C and the restarting SGW-U",
        "Verify that SGW-C re-establishes the PFCP association and context with the new SGW-U",
        "Verify that IPv6 sessions handled by the restarted SGW-U are restored",
        "Send IPv6 traffic through the recovered SGW-U and verify successful flow",
        "Repeat the above steps for a PGW-U instance"
      ],
      "expected_result": "Restarting an SGW-U or PGW-U instance results in successful PFCP re-association and restoration of IPv6 sessions without significant data loss.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_010",
      "category": "Performance/Scale",
      "description": "Validate IPv6 session establishment rate under load",
      "preconditions": [
        "SGW-C/PGW-C and SGW-U/PGW-U are scaled to handle high load",
        "Sufficient IPv6 address pool available"
      ],
      "steps": [
        "Simulate a high rate of UE attach requests requesting IPv6-only sessions",
        "Monitor the rate of successful IPv6 session establishments per second",
        "Measure the time taken for each session establishment",
        "Verify that the system can sustain the target session establishment rate",
        "Monitor CPU, memory, and network utilization on control and user plane components"
      ],
      "expected_result": "The system can establish IPv6 sessions at the specified performance targets, with control plane components handling signaling and user plane components handling data forwarding efficiently.",
      "protocol": ["PFCP", "IPv6"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_011",
      "category": "Performance/Scale",
      "description": "Validate IPv6 data throughput under load",
      "preconditions": [
        "SGW-U/PGW-U are scaled to handle high data volumes",
        "UEs have active IPv6 sessions"
      ],
      "steps": [
        "Simulate high volume IPv6 traffic from multiple UEs",
        "Measure the aggregated IPv6 throughput across SGW-U and PGW-U interfaces",
        "Verify that the throughput meets or exceeds expected performance metrics",
        "Monitor for packet drops or retransmissions at high traffic loads",
        "Analyze performance metrics during sustained high throughput periods"
      ],
      "expected_result": "The system maintains high IPv6 data throughput without significant performance degradation or packet loss under sustained load.",
      "protocol": ["GTP-U", "IPv6"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_012",
      "category": "Interoperability",
      "description": "Interoperate with IPv4-only UEs in a mixed environment",
      "preconditions": [
        "Network supports both IPv4 and IPv6",
        "PGW-C is configured for dual-stack sessions",
        "UEs are configured for IPv4-only connectivity"
      ],
      "steps": [
        "Attach an IPv4-only UE",
        "Verify that an IPv4 session is established",
        "Send IPv4 traffic from the UE",
        "Verify successful IPv4 traffic flow",
        "Simultaneously attach IPv6-only and dual-stack UEs",
        "Verify that IPv6 and dual-stack sessions are established concurrently",
        "Verify that IPv4-only UEs do not experience issues"
      ],
      "expected_result": "IPv4-only UEs can establish and maintain IPv4 sessions without impacting the ability to establish IPv6 or dual-stack sessions for other UEs.",
      "protocol": ["PFCP", "GTP-U", "IPv4", "IPv6"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_013",
      "category": "Interoperability",
      "description": "Interoperate with dual-stack UEs in a mixed environment",
      "preconditions": [
        "Network supports both IPv4 and IPv6",
        "PGW-C is configured for dual-stack sessions",
        "UEs are configured for dual-stack connectivity"
      ],
      "steps": [
        "Attach a dual-stack UE",
        "Verify that both IPv4 and IPv6 sessions are established",
        "Send IPv4 traffic from the UE",
        "Send IPv6 traffic from the UE",
        "Verify successful bi-directional traffic flow for both protocols",
        "Simultaneously attach IPv4-only and IPv6-only UEs",
        "Verify that all session types are established concurrently and function correctly"
      ],
      "expected_result": "Dual-stack UEs can successfully establish and maintain both IPv4 and IPv6 sessions, and coexist with IPv4-only and IPv6-only UEs.",
      "protocol": ["PFCP", "GTP-U", "IPv4", "IPv6"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_014",
      "category": "Network Conditions",
      "description": "Validate IPv6 session stability under packet loss",
      "preconditions": [
        "IPv6 session is established",
        "SGW-C/PGW-C and SGW-U/PGW-U are operational"
      ],
      "steps": [
        "Introduce controlled packet loss on the S5/S8-U or Gi/SGi interfaces",
        "Send continuous IPv6 traffic from the UE",
        "Monitor session status and traffic flow",
        "Verify that the session remains established",
        "Measure the impact on application-level performance (e.g., TCP retransmissions, application errors)"
      ],
      "expected_result": "IPv6 sessions remain established and traffic continues to flow, with expected impact on application performance due to packet loss, but without session teardown.",
      "protocol": ["GTP-U", "IPv6"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_015",
      "category": "Network Conditions",
      "description": "Validate IPv6 session stability under latency",
      "preconditions": [
        "IPv6 session is established",
        "SGW-C/PGW-C and SGW-U/PGW-U are operational"
      ],
      "steps": [
        "Introduce controlled latency on the S5/S8-U or Gi/SGi interfaces",
        "Send continuous IPv6 traffic from the UE",
        "Monitor session status and traffic flow",
        "Verify that the session remains established",
        "Measure the impact on application-level performance (e.g., increased response times)"
      ],
      "expected_result": "IPv6 sessions remain established and traffic continues to flow, with expected impact on application performance due to latency, but without session teardown.",
      "protocol": ["GTP-U", "IPv6"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_016",
      "category": "Network Conditions",
      "description": "Validate PFCP control plane recovery after UPF restart",
      "preconditions": [
        "SGW-U/PGW-U restart is initiated",
        "SGW-C/PGW-C are operational",
        "Active IPv6 sessions are in progress"
      ],
      "steps": [
        "Simulate an unplanned restart of an SGW-U or PGW-U instance",
        "Monitor PFCP messages from SGW-C/PGW-C to the recovering UPF",
        "Verify that the UPF re-establishes PFCP associations and sessions",
        "Confirm that session state is correctly rebuilt on the UPF",
        "Verify that IPv6 data traffic resumes after recovery"
      ],
      "expected_result": "The control plane successfully re-establishes PFCP associations and session contexts with the user plane after an unplanned UPF restart, ensuring minimal disruption to IPv6 services.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_017",
      "category": "Network Conditions",
      "description": "Validate session continuity during Control Plane restart",
      "preconditions": [
        "SGW-C or PGW-C restart is initiated",
        "SGW-U/PGW-U are operational",
        "Active IPv6 sessions are in progress"
      ],
      "steps": [
        "Simulate an unplanned restart of an SGW-C or PGW-C instance",
        "Monitor PFCP messages to the UPF from the restarting control plane",
        "Verify that the control plane re-establishes associations with the UPF",
        "Confirm that existing IPv6 sessions are retained or gracefully re-established",
        "Send IPv6 traffic during and after the control plane restart to verify session continuity"
      ],
      "expected_result": "IPv6 sessions are maintained or quickly restored with minimal interruption during a control plane restart, thanks to HA mechanisms and graceful recovery.",
      "protocol": ["PFCP", "GTP-U", "IPv6"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_018",
      "category": "Security",
      "description": "Validate IPv6 Address Spoofing Prevention",
      "preconditions": [
        "IPv6 sessions are established",
        "SGW-U and PGW-U are configured with appropriate filtering rules"
      ],
      "steps": [
        "Attempt to send IPv6 packets from a UE with a source IP address that does not belong to its assigned IPv6 address",
        "Monitor traffic at the PGW-U egress interface (Gi/SGi)",
        "Verify that such spoofed packets are dropped or rejected"
      ],
      "expected_result": "The system prevents IPv6 address spoofing by dropping or rejecting packets originating from UEs with source IP addresses that do not match their allocated IPv6 addresses.",
      "protocol": ["IPv6", "PFCP"],
      "priority": "High"
    },
    {
      "id": "CUPS_IPV6_TC_019",
      "category": "Security",
      "description": "Validate IPv6 Filtering Rules (e.g., ACLs)",
      "preconditions": [
        "IPv6 sessions are established",
        "SGW-U and PGW-U are configured with specific IPv6 access control lists (ACLs)",
        "UEs have active IPv6 sessions"
      ],
      "steps": [
        "Configure a policy on PGW-U to block a specific IPv6 destination or port for a given UE or service",
        "Attempt to send IPv6 traffic from the UE to the blocked destination/port",
        "Verify that the traffic is dropped by PGW-U",
        "Attempt to send IPv6 traffic to an allowed destination/port",
        "Verify that the traffic is successfully forwarded"
      ],
      "expected_result": "IPv6 traffic is correctly filtered based on configured access control lists on the user plane components.",
      "protocol": ["IPv6", "PFCP"],
      "priority": "Medium"
    },
    {
      "id": "CUPS_IPV6_TC_020",
      "category": "Functional",
      "description": "Validate IPv6 traffic routing over S5/S8 interface",
      "preconditions": [
        "SGW-U and PGW-U are running",
        "IPv6 sessions are established for UEs",
        "S5/S8 interface is configured for IPv6 data forwarding"
      ],
      "steps": [
        "Send IPv6 traffic from a UE attached to SGW-U",
        "Monitor the traffic flow from SGW-U to PGW-U over the S5/S8-U interface",
        "Verify that the traffic is correctly encapsulated (e.g., GTP-U with IPv6 payload)",
        "Verify that the IPv6 source and destination addresses are maintained",
        "At PGW-U, verify that the traffic is correctly de-encapsulated and routed towards the Gi/SGi interface"
      ],
      "expected_result": "IPv6 data traffic is successfully forwarded between SGW-U and PGW-U over the S5/S8-U interface, maintaining correct encapsulation and addressing.",
      "protocol": ["GTP-U", "IPv6"],
      "priority": "High"
    }
  ]
}
```