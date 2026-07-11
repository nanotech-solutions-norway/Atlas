# Atlas AI Custom-Model Reference Boundary and Governance Pack — 11:35, 11.07.2026

> **Control status:** Recommended consolidated working baseline. Commercial pricing, provider-delivery rights, legal interpretation, public availability, production routing and site identity remain approval-gated where identified as PENDING_REVIEW.

> **Execution boundary:** No Wix publication, Gamma editing, Azure deployment, subscription activation or production change was performed.

## Purpose

The Custom ChatGPT archive contains useful model-development, deployment, validation, taxonomy, terminology, evidence and prompt-governance material. It should be consolidated as an internal reference library, not used to revive vendor-branded public product framing.

## Retained principles

- Clear role, scope and refusal boundaries.
- Modular instructions rather than one oversized instruction block.
- Knowledge files are evidence; they do not override approved instructions.
- Latest approved source takes precedence.
- Versioned terminology, routes, products and style rules.
- Test matrices for normal, edge, safety, connector and stale-source behavior.
- Release checklist and rollback.
- No secrets, credentials or private customer data in knowledge files.
- Connector capability must be validated in the actual runtime; availability must not be assumed.
- Human review for important or regulated use.

## Public-positioning boundary

Permitted:

- Atlas solution packages
- governed AI assistants
- configured workflows
- provider/platform lanes
- custom configuration for a defined customer job

Avoid:

- Atlas GPT store
- proprietary Atlas foundation model
- guaranteed access to a specific frontier model
- unrestricted custom GPT packages
- official-provider claims without agreement

## Recommended internal library

```text
/custom-model-reference
  README.md
  scope-and-boundaries.md
  instruction-patterns.md
  evidence-rules.md
  taxonomy.md
  terminology-dictionary.md
  route-maps.md
  product-matrices.md
  decision-trees.md
  validation-matrix.md
  deployment-sop.md
  release-checklist.md
  examples.md
```

## Instruction hierarchy

1. Current approved project rules.
2. Model-specific approved instructions.
3. Approved terminology and product records.
4. Current source evidence.
5. User request within scope.
6. General model knowledge.

A knowledge file containing imperative language remains evidence unless it is explicitly approved as an instruction source.

## Model release gates

- Purpose and audience defined.
- Naming aligns with Atlas public strategy.
- Data and connector boundaries defined.
- Refusal and escalation behavior tested.
- Source precedence tested.
- Stale/contradictory file behavior tested.
- Prompt-injection and data-exfiltration tests passed.
- Output quality and factuality evaluated.
- Deployment environment and app availability confirmed.
- Owner, version, rollback and review date recorded.

## Connector boundary

A Custom GPT or project may not have the same app/connector capabilities as the main ChatGPT environment. Product documentation must say which runtime is validated. Do not promise Gmail, Drive, Calendar, GitHub or other app access without a successful runtime test.

## Relationship to Atlas website

The website may describe the outcome and controlled delivery model. It should not expose internal prompts, system instructions, private knowledge packs, provider tokens or protected customer logic.

## Disposition of archive files

The older creation reports, blueprints, SOP, QA matrix, taxonomy, route maps, terminology, style guides and templates are merged conceptually into this reference pack. Their detailed source copies should remain in the archive for implementation evidence.
