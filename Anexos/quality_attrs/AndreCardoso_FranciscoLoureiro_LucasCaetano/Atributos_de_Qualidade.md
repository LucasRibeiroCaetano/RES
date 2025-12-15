# Quality Attributes for Digital Wallet System

## Authors
- Lucas Caetano
- André Cardoso
- Francisco Loureiro

Team: LFA

## Brief Description of the System and Its Technical and Business Drivers
The Digital Wallet system is a secure mobile application designed for users to store digital currencies, perform peer-to-peer transactions, make payments to merchants, and manage financial accounts. It integrates with banking APIs, blockchain networks for cryptocurrency support, and payment gateways for seamless transactions.  

Technical drivers include the need for robust encryption to protect sensitive data, scalable architecture to handle high transaction volumes, and cross-platform compatibility for iOS and Android devices. Business drivers focus on increasing user adoption through intuitive interfaces, ensuring regulatory compliance (e.g., GDPR, PCI-DSS) to avoid legal issues, generating revenue via transaction fees, and building trust to compete with established wallets like PayPal or Apple Pay.

## Extensive List of Potential Quality Attributes from ISO 25010
Based on the ISO 25010 software quality model, the following is an extensive list of potential quality attributes relevant to our Digital Wallet system. We have included the main characteristics and their sub-attributes:

- **Functional Suitability**: The degree to which the system provides functions that meet stated and implied needs.
  - Functional completeness
  - Functional correctness
  - Functional appropriateness

- **Performance Efficiency**: The performance relative to the amount of resources used under stated conditions.
  - Time behavior
  - Resource utilization
  - Capacity

- **Reliability**: The degree to which the system performs specified functions under specified conditions for a specified period.
  - Maturity
  - Availability
  - Fault tolerance
  - Recoverability

- **Usability**: The degree to which the system can be used by specified users to achieve specified goals with effectiveness, efficiency, and satisfaction.
  - Appropriateness recognizability
  - Learnability
  - Operability
  - User error protection
  - User interface aesthetics
  - Accessibility

- **Security**: The degree to which the system protects information and data so that persons or other products or systems have the degree of data access appropriate to their types and levels of authorization.
  - Confidentiality
  - Integrity
  - Non-repudiation
  - Accountability
  - Authenticity

- **Compatibility**: The degree to which the system can exchange information with other products or systems and/or perform its required functions while sharing the same hardware or software environment.
  - Co-existence
  - Interoperability

- **Maintainability**: The degree of effectiveness and efficiency with which the system can be modified to improve it, correct it, or adapt it to changes in environment and requirements.
  - Modularity
  - Reusability
  - Analysability
  - Modifiability
  - Testability

- **Portability**: The degree of effectiveness and efficiency with which the system can be transferred from one hardware, software, or other operational or usage environment to another.
  - Adaptability
  - Installability
  - Replaceability

For prioritization, we selected the following seven attributes as most relevant: Security, Usability, Reliability, Performance Efficiency, Compatibility, Maintainability, and Portability.

## Description of the Prioritization Criteria and Its Relative Weights
We defined four prioritization criteria to evaluate the quality attributes. Each criterion is described below, along with its relative weight (using Fibonacci sequence values: 3, 5, 8, 13) and the relevant actors (from our use-case analysis: End User, Merchant, Administrator, Developer).

- **Risk if Not Addressed**: Measures the potential negative impact (e.g., financial loss, legal issues) if the attribute is poorly implemented. Weight: 13. Relevant actors: All (End User, Merchant, Administrator, Developer).
- **Business Value**: Assesses how the attribute contributes to business goals like revenue growth and market competitiveness. Weight: 8. Relevant actors: Merchant, Administrator.
- **User Impact**: Evaluates the effect on user satisfaction, adoption, and retention. Weight: 5. Relevant actors: End User, Merchant.
- **Technical Feasibility**: Considers the ease of implementation given current technology and team expertise. Weight: 3. Relevant actors: Developer.

These criteria were chosen to balance strategic, user-centric, and practical considerations for a financial application like our Digital Wallet.

## Table with the Ranked Quality Attributes According to the Previous Criteria
We assigned scores (1-5, where 5 is highest) to each quality attribute for each criterion, calculated the weighted total (score × weight), and ranked them in descending order.

| Quality Attribute      | Risk if Not Addressed (13) | Business Value (8) | User Impact (5) | Technical Feasibility (3) | Total Score | Rank |
|------------------------|----------------------------|--------------------|-----------------|---------------------------|-------------|------|
| Security              | 5 (65)                    | 5 (40)            | 4 (20)         | 3 (9)                    | 134        | 1    |
| Reliability           | 4 (52)                    | 4 (32)            | 4 (20)         | 4 (12)                   | 116        | 2    |
| Usability             | 3 (39)                    | 3 (24)            | 5 (25)         | 5 (15)                   | 103        | 3    |
| Performance Efficiency| 4 (52)                    | 3 (24)            | 3 (15)         | 3 (9)                    | 100        | 4    |
| Compatibility         | 3 (39)                    | 4 (32)            | 3 (15)         | 4 (12)                   | 98         | 5    |
| Maintainability       | 2 (26)                    | 3 (24)            | 2 (10)         | 5 (15)                   | 75         | 6    |
| Portability           | 2 (26)                    | 2 (16)            | 3 (15)         | 4 (12)                   | 69         | 7    |

## Final Verdict Rationale for Selecting the Top 3
The ranking aligns well with the needs of a Digital Wallet system, where handling sensitive financial data and ensuring user trust are paramount. We selected the top three: Security, Reliability and Usability, as they directly address core risks and drivers. Security is essential to prevent breaches and fraud, which could lead to catastrophic losses and regulatory penalties. Reliability ensures the system is dependable for constant use, building long-term trust. Usability is critical for user adoption, as a complex interface could drive users to competitors. We reviewed the list and found no major oversights; for instance, while Performance Efficiency ranked high, it is secondary to these foundational attributes in a security-sensitive app. If needed, we could revisit criteria weights, but the current top three make sense for prioritization in development.

## Table with At Least Three Concrete Scenarios for Each Selected Quality Attribute
The table below outlines concrete scenarios for each of the top three quality attributes. Each scenario follows the structure: Source of Stimulus, Stimulus, Artifact (system part affected), Environment, Response, and Response Measure. We provide at least three per attribute.

| Quality Attribute | Source of Stimulus | Stimulus | Artifact | Environment | Response | Response Measure |
|-------------------|--------------------|----------|----------|-------------|----------|------------------|
| Security         | Unauthorized user | Attempts login with stolen credentials | Authentication module | Normal operation, online | System detects anomaly and blocks access, notifies user | 100% of unauthorized attempts blocked within 5 seconds |
| Security         | Malicious actor   | Injects SQL code in input fields      | Database interface    | High traffic, online | Input is sanitized, attack prevented | Zero successful injections in 99.9% of test cases |
| Security         | Internal employee | Accesses user data without permission | Access control system | Internal network     | Role-based access denies request, logs incident | All unauthorized internal accesses audited and blocked in under 1 second |
| Security         | Phishing attacker | Sends fake transaction confirmation   | Email/SMS notification system | User device, online | System verifies via 2FA before processing | 95% reduction in successful phishing via mandatory 2FA confirmation |
| Reliability      | System user       | Server outage due to high load        | Transaction processing engine | Peak hours, 10,000 concurrent users | System switches to backup server automatically | Downtime less than 30 seconds, 99.99% availability |
| Reliability      | Hardware failure  | Disk failure in data storage          | Data recovery module  | Normal operation     | Data is recovered from redundant backups | Full recovery within 5 minutes, no data loss |
| Reliability      | Network disruption| Temporary internet loss during transaction | Mobile app connectivity handler | Mobile network, offline mode | Transaction queues and syncs upon reconnection | 100% of queued transactions completed successfully within 1 minute of reconnection |
| Usability        | New user          | First-time app setup                  | Onboarding interface  | Mobile device, first launch | Guides user through simple steps with tooltips | 90% of users complete setup in under 2 minutes |
| Usability        | Elderly user      | Performs a payment transaction        | Payment screen        | Touchscreen device, normal use | Interface provides large buttons, voice assistance | Task completion rate of 95% with fewer than 3 errors |
| Usability        | Visually impaired user | Navigates account balance | Screen reader integration | Accessibility mode enabled | App reads out information clearly | 100% compatibility with screen readers, satisfaction score >4/5 |
| Usability        | Busy merchant     | Processes multiple refunds            | Refund management dashboard | High-volume store, online | Batch processing with intuitive filters | Average time per refund <10 seconds |

## Description of the Conflicting Quality Attribute Scenarios and How You Dealt with Them
In our analysis, we identified several conflicts among the top quality attributes, particularly between Security and Usability, and between Reliability and Performance Efficiency (though the latter was not in the top three, it influenced decisions).

1. **Security vs. Usability**: Strong security measures like multi-factor authentication (MFA) and complex password requirements can frustrate users, leading to slower logins or higher abandonment rates. For example, a scenario requiring biometric + PIN for every transaction (Security) conflicts with quick one-tap payments (Usability).  
   - **How we addressed it**: We prioritized Security but mitigated usability issues by implementing optional biometrics (e.g., fingerprint or face ID) for low-value transactions, reducing steps for trusted devices. We updated the Usability scenarios to include user error protection via auto-save sessions, ensuring a balance without compromising core security.

2. **Reliability vs. Security**: Enhancing reliability through data redundancy (e.g., multiple backups) can introduce security risks if backups are not equally protected, potentially creating more attack vectors.  
   - **How we addressed it**: We updated Reliability scenarios to mandate encrypted backups and automated integrity checks. Decisions included adopting zero-trust architecture, where reliability features like failover are secured by default, and conducting trade-off analysis to limit redundancy to critical data only.

3. **General Conflicts**: Usability's emphasis on simplicity can conflict with Reliability's need for detailed error logging, which might expose sensitive info.  
   - **How we addressed it**: We recorded strategies such as anonymized logging and user-friendly error messages (e.g., "Try again" instead of technical details). Overall, we prioritized based on risk (favoring Security), tested prototypes with users, and iterated on scenarios to ensure no attribute is fully sacrificed—aiming for a minimum viable threshold for each.