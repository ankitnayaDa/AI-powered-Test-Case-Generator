*** Settings ***
Library    BuiltIn

*** Test Cases ***

CUPS_IPV6_TC_001 - Validate IPv6 session establishment with SGW-U and PGW-U
    [Documentation]    Validate IPv6 session establishment with SGW-U and PGW-U
    [Tags]    PFCP    GTP-U    IPv6

    Initiate Pdn Session Creation Request From A Ue Requesting Ipv6 Connectivity
    Monitor Pfcp Messages For Session Establishment Requests Containing Ipv6 Context Eg Requested Ip Type
    Verify Upf Allocates An Ipv6 Address To The Ue
    Verify Pfcp Session Modification Messages Update The Session With Ipv6 Address Information
    Send Ipv6 Traffic From The Ue Towards The External Ipv6 Network
    Verify Upf Forwards Ipv6 Traffic Correctly Utilizing S5S8 For Control And Gisgi For User Plane

    Verify Test Case Expected Result

CUPS_IPV6_TC_002 - Validate Dual-Stack (IPv4/IPv6) session establishment with SGW-U and PGW-U
    [Documentation]    Validate Dual-Stack (IPv4/IPv6) session establishment with SGW-U and PGW-U
    [Tags]    PFCP    GTP-U    IPv4    IPv6

    Initiate Pdn Session Creation Request From A Ue Requesting Dualstack Connectivity
    Monitor Pfcp Messages For Session Establishment Requests Indicating Dualstack Support
    Verify Upf Allocates Both An Ipv4 And An Ipv6 Address To The Ue
    Verify Pfcp Session Modification Messages Update The Session With Both Ipv4 And Ipv6 Address Information
    Send Ipv4 Traffic From The Ue
    Send Ipv6 Traffic From The Ue
    Verify Upf Correctly Handles And Routes Both Ipv4 And Ipv6 Traffic Streams

    Verify Test Case Expected Result

CUPS_IPV6_TC_003 - Validate PFCP session establishment with IPv6 parameters and specific QoS
    [Documentation]    Validate PFCP session establishment with IPv6 parameters and specific QoS
    [Tags]    PFCP    IPv6

    Initiate Pdn Session Creation Request From Ue With Ipv6 And Specified Qos Parameters
    Observe Pfcp Session Establishment Request Messages Ensuring Ipv6 Address Family And Qos Ie Are Correctly Populated
    Verify Upf Creates A Qos Flow For The Ipv6 Session Based On The Requested Parameters
    Confirm Pfcp Session Establishment Response Confirms Session Setup With Correct Ipv6 Details And Qos

    Verify Test Case Expected Result

CUPS_IPV6_TC_004 - Validate IPv6 address allocation mechanisms (DHCPv6/SLAAC)
    [Documentation]    Validate IPv6 address allocation mechanisms (DHCPv6/SLAAC)
    [Tags]    PFCP    IPv6    DHCPv6    SLAAC

    Configure Upf To Use Dhcpv6 For Ipv6 Address Assignment
    Initiate Session Setup For An Ipv6 Ue
    Monitor Upfs Interaction With Dhcpv6 Server If External
    Verify Upf Assigns An Ipv6 Address To The Ue
    Configure Upf To Use Slaac For Ipv6 Address Assignment
    Initiate Session Setup For An Ipv6 Ue
    Verify Upf Facilitates Slaac Process And Assigns An Ipv6 Address To The Ue

    Verify Test Case Expected Result

CUPS_IPV6_TC_005 - Validate Control and User Plane Separation (CUPS) for IPv6 traffic
    [Documentation]    Validate Control and User Plane Separation (CUPS) for IPv6 traffic
    [Tags]    PFCP    GTP-U    IPv6

    Initiate Ipv6 Traffic Flow From Ue
    Monitor Control Plane Traffic Pfcp S5S8 Control During Session Setupmodification
    Monitor User Plane Traffic Gtpu S5S8 User Gisgi Carrying Ipv6 Packets
    Induce A Temporary Outage Or High Load On Sgwcpgwc And Observe Impact On User Plane Forwarding Of Ipv6 Traffic
    Induce A Temporary Outage Or High Load On Sgwupgwu And Observe Impact On Control Plane Signaling For Ipv6 Sessions

    Verify Test Case Expected Result

CUPS_IPV6_TC_006 - Validate IPv6 session lifecycle: Create, Modify, Delete
    [Documentation]    Validate IPv6 session lifecycle: Create, Modify, Delete
    [Tags]    PFCP    GTP-U    IPv6

    Create An Ipv6 Session For A Ue
    Verify Session Establishment And Ipv6 Address Assignment
    Modify The Ipv6 Session Eg Change Qos Addremove Pdu Sessions Within The Same Bearer
    Verify Pfcp Session Modification Request And Response Messages
    Verify Upf Updates Session Parameters Accordingly
    Delete The Ipv6 Session
    Verify Pfcp Session Deletion Request And Response Messages
    Confirm Ue Loses Ipv6 Connectivity

    Verify Test Case Expected Result

CUPS_IPV6_TC_007 - Validate SGW-C/PGW-C failover and recovery with active IPv6 sessions
    [Documentation]    Validate SGW-C/PGW-C failover and recovery with active IPv6 sessions
    [Tags]    PFCP    GTP-U    IPv6

    Gracefully Restart One Instance Of Sgwc
    Monitor Pfcp Reassociation And Session Recovery
    Verify Active Ipv6 Sessions Remain Active With Minimal Disruption Eg Brief Packet Loss
    Send New Ipv6 Session Establishment Requests During Sgwc Restart
    Repeat Steps For Pgwc
    Simulate Unhealthy State For Sgwcpgwc Pods Eg Network Partition Resource Exhaustion And Verify Autohealingfailover

    Verify Test Case Expected Result

CUPS_IPV6_TC_008 - Validate UPF (SGW-U/PGW-U) restart and recovery with active IPv6 sessions
    [Documentation]    Validate UPF (SGW-U/PGW-U) restart and recovery with active IPv6 sessions
    [Tags]    PFCP    GTP-U    IPv6

    Gracefully Restart One Instance Of A Upf Sgwu Or Pgwu
    Monitor Pfcp Messages For Reassociation With The Cp
    Verify Active Ipv6 Sessions Are Migrated Or Resumed On A Healthy Upf Instance
    Send Ipv6 Traffic During Upf Restart And Observe Rerouting And Recovery
    Simulate Unhealthy State For Upf Pods And Verify Reschedulingrecreation

    Verify Test Case Expected Result

CUPS_IPV6_TC_009 - Validate performance and scale of IPv6 traffic handling under load
    [Documentation]    Validate performance and scale of IPv6 traffic handling under load
    [Tags]    PFCP    GTP-U    IPv6

    Configure Test Ues To Establish Ipv6 Sessions
    Generate A High Volume Of Sustained Ipv6 User Plane Traffic
    Monitor Upf Throughput Latency And Resource Utilization Cpu Memory
    Monitor Sgwc And Pgwc Signaling Load Pfcp Messages Per Second
    Gradually Increase The Number Of Concurrent Ipv6 Sessions And Traffic Load Up To System Limits
    Observe System Behavior For Any Performance Degradation Packet Drops Or Control Plane Instability

    Verify Test Case Expected Result

CUPS_IPV6_TC_010 - Interoperability with IPv4-only UEs
    [Documentation]    Interoperability with IPv4-only UEs
    [Tags]    PFCP    GTP-U    IPv4    IPv6

    Connect An Ipv4Only Ue To The Network
    Initiate An Ipv4 Pdn Session Creation Request
    Verify The Ue Receives An Ipv4 Address
    Send Ipv4 Traffic From The Ue
    Verify Upf Correctly Routes Ipv4 Traffic For This Ue
    Verify The Presence Of The Ipv4Only Ue Does Not Impact The Active Ipv6 Sessions Performance Or Stability

    Verify Test Case Expected Result

CUPS_IPV6_TC_011 - Interoperability with Dual-Stack UEs (mixed traffic types)
    [Documentation]    Interoperability with Dual-Stack UEs (mixed traffic types)
    [Tags]    PFCP    GTP-U    IPv4    IPv6

    Connect A Dualstack Ue To The Network
    Initiate A Dualstack Pdn Session Creation Request
    Verify The Ue Receives Both Ipv4 And Ipv6 Addresses
    Send Ipv4 Traffic From The Ue
    Send Ipv6 Traffic From The Ue
    Verify Upf Correctly Routes Both Ipv4 And Ipv6 Traffic Streams For This Ue
    Verify The Dualstack Ues Traffic Does Not Negatively Impact Other Ipv4Only Or Ipv6Only Sessions

    Verify Test Case Expected Result

CUPS_IPV6_TC_012 - Validate IPv6 address spoofing prevention
    [Documentation]    Validate IPv6 address spoofing prevention
    [Tags]    IPv6    PFCP

    Attempt To Send Ipv6 Packets From A Source Ip Address That Is Not Assigned To The Ue Or Is Outside Its Allocated Prefix
    Monitor Upf For Packet Drops Or Rejection Of Spoofed Packets
    Verify Upf Does Not Forward Spoofed Ipv6 Traffic

    Verify Test Case Expected Result

CUPS_IPV6_TC_013 - Validate IPv6 traffic filtering and policy enforcement
    [Documentation]    Validate IPv6 traffic filtering and policy enforcement
    [Tags]    IPv6    PFCP

    Configure Policies On Pgwcupf To Block Specific Ipv6 Destinations Or Protocols
    Attempt To Send Ipv6 Traffic From The Ue To A Blocked Destinationprotocol
    Verify That The Upf Blocks And Discards This Traffic
    Attempt To Send Ipv6 Traffic To An Allowed Destinationprotocol
    Verify That This Traffic Is Allowed To Pass Through

    Verify Test Case Expected Result

CUPS_IPV6_TC_014 - IPv6 session handling under packet loss
    [Documentation]    IPv6 session handling under packet loss
    [Tags]    IPv6    PFCP    GTP-U

    Introduce Controlled Packet Loss On The User Plane Interface Eg Gisgi Or S5S8 User Plane
    Send Sustained Ipv6 Traffic From The Ue
    Monitor For Session Reestablishment Traffic Retransmissions And Overall Session Stability
    Observe Control Plane Signaling Pfcp For Any Impact Or Retransmissions Due To Packet Loss

    Verify Test Case Expected Result

CUPS_IPV6_TC_015 - IPv6 session handling under high latency
    [Documentation]    IPv6 session handling under high latency
    [Tags]    IPv6    PFCP    GTP-U

    Introduce Controlled High Latency On The User Plane Interface Eg Gisgi Or S5S8 User Plane
    Send Sustained Ipv6 Traffic From The Ue
    Monitor Session Responsiveness And Latency For Ipv6 Application Traffic
    Observe Control Plane Signaling Pfcp For Any Delays Or Timeouts

    Verify Test Case Expected Result

CUPS_IPV6_TC_016 - IPv6 session continuity during UPF restart (simulated)
    [Documentation]    IPv6 session continuity during UPF restart (simulated)
    [Tags]    PFCP    GTP-U    IPv6

    Initiate A Restart Of A Upf Instance While An Ipv6 Session Is Active And Transmitting Data
    Observe The Upf Restarting And Reassociating With The Control Plane
    Monitor The Ipv6 Traffic Flow During The Upf Restart Period
    Verify That The Session Resumes And Traffic Flows Again Once The Upf Is Operational

    Verify Test Case Expected Result

CUPS_IPV6_TC_017 - IPv6 session continuity during Control Plane restart (simulated)
    [Documentation]    IPv6 session continuity during Control Plane restart (simulated)
    [Tags]    PFCP    GTP-U    IPv6

    Initiate A Restart Of An Sgwc Or Pgwc Instance While An Ipv6 Session Is Active
    Observe The Control Plane Instance Restarting And Reassociating With Upfs
    Monitor The Ipv6 Traffic Flow During The Control Plane Restart Period
    Verify That The Session Remains Active Or Quickly Recovers Once The Control Plane Instance Is Operational

    Verify Test Case Expected Result

CUPS_IPV6_TC_018 - Validate IPv6 extension headers handling
    [Documentation]    Validate IPv6 extension headers handling
    [Tags]    IPv6    PFCP

    Configure Ue To Send Ipv6 Traffic With Different Types Of Extension Headers
    Verify Upf Correctly Processes And Forwards Packets With Valid Extension Headers
    Attempt To Send Ipv6 Packets With Malformed Or Invalid Extension Headers
    Verify Upf Drops Or Rejects Malformed Extension Headers According To Rfc Standards

    Verify Test Case Expected Result

CUPS_IPV6_TC_019 - Validate IPv6 Neighbor Discovery Protocol (NDP) functionality
    [Documentation]    Validate IPv6 Neighbor Discovery Protocol (NDP) functionality
    [Tags]    IPv6    NDP    PFCP

    Initiate Communication From Ue To Another Device On The Same Ipv6 Subnet
    Verify Ue Performs Neighbor Solicitation
    Verify Upf Facilitates The Neighbor Advertisement Process If Applicable At Upf Layer
    Confirm Successful Neighbor Unreachability Detection Nud

    Verify Test Case Expected Result

CUPS_IPV6_TC_020 - Validate IPv6 Router Advertisements (RA) and Stateless Address Autoconfiguration (SLAAC)
    [Documentation]    Validate IPv6 Router Advertisements (RA) and Stateless Address Autoconfiguration (SLAAC)
    [Tags]    IPv6    RA    SLAAC    PFCP

    Configure Upf To Send Ipv6 Router Advertisements To The Ues Subnet
    Initiate Session Setup For An Ipv6 Ue
    Verify The Ue Receives Router Advertisements
    Verify The Ue Can Use Ras To Configure Its Ipv6 Address Slaac And Discover Default Gateway

    Verify Test Case Expected Result
