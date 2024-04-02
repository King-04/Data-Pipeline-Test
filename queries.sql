-- 1. Get all customer names and email addresses:
SELECT Name, EmailAddress FROM MaphlixData;

-- 2. Find customers who prefer email as a communication method:
SELECT * FROM MaphlixData WHERE CommunicationMethod = 'Email';

-- 3. Count the number of transactions for each branch:
SELECT Branch, COUNT(*) AS TransactionCount FROM MaphlixData GROUP BY Branch;

-- 4. Retrieve customers who have made more than a certain number of transactions (e.g., more than 5):
SELECT * FROM MaphlixData WHERE TransactionActivity > 100;

-- 5. List all unique services or products offered by branches:
SELECT DISTINCT Branch, ServicesOrProducts FROM MaphlixData;

-- 6. Find customers who haven't provided a phone number:
SELECT * FROM MaphlixData WHERE PhoneNumber IS NULL;

-- 7. Get the most frequently occurring communication method:
SELECT CommunicationMethod, COUNT(*) AS Frequency FROM MaphlixData
GROUP BY CommunicationMethod ORDER BY Frequency DESC LIMIT 1;

-- 8. Retrieve customers who have a specific preference:
SELECT * FROM MaphlixData WHERE CustomerPreference = 'Branch walk-in';

-- 9. Find customers from a specific branch with a given email address:
SELECT * FROM MaphlixData WHERE Branch = 'BranchName' AND EmailAddress = 'irussell@example.net';

-- 10. List all customers and their respective addresses sorted alphabetically by name:
SELECT Name, Address FROM MaphlixData ORDER BY Name;
