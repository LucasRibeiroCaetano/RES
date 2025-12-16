# Quality Attributes for Digital Wallet System

## Authors
- Lucas Caetano
- André Cardoso
- Francisco Loureiro

Team: LFA

## Brief Description of the System and Its Technical and Business Drivers
The Digital Wallet system is a secure mobile application designed for users to store funds, perform peer-to-peer transactions, make payments to merchants, and manage financial accounts. It prioritizes data integrity through fixed-point arithmetic and atomic transactions.

Technical drivers include the need for robust encryption (to support UC8: Manage Security), scalable architecture to handle concurrent transactions (UC5: Pay Merchant), and strict consistency for account balances (UC4: Transfer Money). Business drivers focus on building trust to compete with established wallets and ensuring regulatory compliance (GDPR, PCI-DSS).

---

### 1. Extensive List of Potential Quality Attributes from ISO 25010
Based on the ISO 25010 software quality model, the following is the list of potential quality attributes relevant to our Digital Wallet system. We focused strictly on non-functional characteristics:

- **Security**: The degree to which the system protects information and data so that persons or other products have the degree of data access appropriate to their types and levels of authorization.
  - Confidentiality (Crucial for UC1: Register and UC2: Authenticate)
  - Integrity (Crucial for UC4: Transfer Money - Atomic Transactions)
  - Non-repudiation
  - Accountability
  - Authenticity

- **Reliability**: The degree to which the system performs specified functions under specified conditions for a specified period.
  - Maturity
  - Availability (Crucial for UC5: Pay Merchant - service must be up)
  - Fault tolerance
  - Recoverability

- **Usability**: The degree to which the system can be used by specified users to achieve specified goals with effectiveness, efficiency, and satisfaction.
  - Appropriateness recognizability
  - Learnability
  - Operability (Crucial for UC3: Add Funds and UC5: Pay Merchant)
  - User error protection
  - Accessibility

- **Performance Efficiency**: The performance relative to the amount of resources used under stated conditions.
  - Time behavior (Response time for transactions)
  - Resource utilization
  - Capacity (Concurrent users)

- **Compatibility**: The degree to which the system can exchange information with other products or systems.
  - Co-existence
  - Interoperability (Crucial for connecting to Banking Systems/Gateways)

- **Maintainability**: The degree of effectiveness and efficiency with which the system can be modified.
  - Modularity
  - Reusability
  - Testability (Crucial for validating the "Lockout" logic in UC8)

- **Portability**: The degree of effectiveness and efficiency with which the system can be transferred from one environment to another.
  - Adaptability (iOS/Android)
  - Installability

For prioritization, we selected the following seven attributes as most relevant: Security, Reliability, Usability, Performance Efficiency, Compatibility, Maintainability, and Portability.

---

### 2. Prioritization Criteria and Relative Weights
We defined four prioritization criteria to evaluate the quality attributes. Each criterion is described below, along with its relative weight (using Fibonacci sequence values: 3, 5, 8, 13) and the relevant actors.

1.  **Risk if Not Addressed (Weight: 13)**
    * *Description:* Measures the potential negative impact (financial loss, legal liability, data corruption) if the attribute is ignored.
    * *Relevant Actors:* End User, Merchant, Administrator.
    * *Context:* A failure in *Security* or *Reliability* leads to direct money loss.

2.  **Business Value (Weight: 8)**
    * *Description:* Assesses how the attribute contributes to revenue growth, market competitiveness, and brand trust.
    * *Relevant Actors:* Administrator (Business Owner), Merchant.
    * *Context:* Trust is the main currency of a Digital Wallet.

3.  **User Impact (Weight: 5)**
    * *Description:* Evaluates the effect on user satisfaction, adoption rates, and retention.
    * *Relevant Actors:* End User, Merchant.
    * *Context:* Poor *Usability* in UC5 (Pay Merchant) causes lines at the store, frustrating users.

4.  **Technical Feasibility (Weight: 3)**
    * *Description:* Considers the ease of implementation given current technology and team expertise.
    * *Relevant Actors:* Developer.
