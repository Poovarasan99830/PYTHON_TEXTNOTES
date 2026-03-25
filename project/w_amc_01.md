
# --------------------------------------------------------------
Difference Between Warranty & AMC (Short)
•	Warranty → Product vaangina apram free-ah company kudukkum (limited time)
•	AMC → Warranty mudinja apram paid service contract

# --------------------------------------------------------------

AMC-la Enna Enna Include Aagum?
Usually:
•	Regular servicing
•	Periodic checkups
•	Minor repairs
•	Emergency service support
Warranty illa naalum, AMC irundhaa extra repair cost kammi aagum.


# --------------------------------------------------------------



🔹 Proactive Lifecycle Management – Meaning (Tanglish)
Proactive na
👉 problem varradhukku munnaadi action eduthuradhu
Lifecycle management na
👉 oru product / appliance oda full life-a manage panradhu
(from purchase → usage → maintenance → expiry → renewal)


# --------------------------------------------------------------


“While creating the models, I faced a few challenges.


First, circular imports between apps like Appliance and WarrantyAMC — I solved it by using string references in ForeignKeys.

# --------------------------------------------------------------

Second, with a custom User model, I encountered migration order issues; I fixed it by setting AUTH_USER_MODEL before migrations and resetting dev migrations.


# --------------------------------------------------------------
Third, I needed automatic status updates for warranties, which I implemented using a property and overriding save().

# --------------------------------------------------------------
Finally, for efficiency, I added indexes and created a separate NotificationLog model to keep logs scalable and clean.”
# --------------------------------------------------------------