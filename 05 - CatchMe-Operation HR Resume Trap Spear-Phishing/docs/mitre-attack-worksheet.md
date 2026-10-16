# MITRE ATT&CK Evidence Worksheet

Add techniques only after validating the relevant behaviour in the
artefacts.

  -------------------------------------------------------------------------------
  Observed         Technique / ID Evidence          Confidence     Notes
  behaviour                       reference                        
  ---------------- -------------- ----------------- -------------- --------------
  Resume-themed    Pending        Email artefact    Pending        Theme alone
  phishing email                                                   does not prove
                                                                   execution

  Malicious        Pending        Attachment and    Pending        Confirm type
  document or                     macro output                     and behaviour
  macro                                                            

  Stage 2 payload  Pending        Process/memory    Pending        Record
  execution                       evidence                         process, PID,
                                                                   PPID, path

  C2 communication Pending        Network/process   Pending        Correlate
                                  evidence                         endpoint and
                                                                   network
                                                                   observations

  Scheduled-task   Pending        Task artefact /   Pending        Record exact
  persistence                     command line                     command
  -------------------------------------------------------------------------------

## Mapping notes

-   Cite the exact artefact and observation.
-   Do not map behaviours merely because they appear in a question.
-   Distinguish attempted activity from successful execution.
