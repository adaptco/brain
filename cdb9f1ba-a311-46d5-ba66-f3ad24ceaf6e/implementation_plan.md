# VT-TQ-Search: Challenge Generator Implementation Plan

## Goal

Implement the logic gap identified in the verification report: the "Challenges & Clusters" feature. This involves creating a `ChallengeGenerator` service that uses vector similarity to find tool clusters and generate exploratory challenges.

## Proposed Changes

### 1. New Service Logic

#### [NEW] [challenge_generator.py](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/toolquest/semantic/challenge_generator.py)

- **`ChallengeGenerator` Class**:
  - `find_tool_clusters(tool_id)`: Find semantic neighbors using Qdrant.
  - `calculate_novelty(tool_id, user_history)`: Compute novelty score based on user's past usage (inverse frequency).
  - `generate_challenge(tool_id)`: Create a `SemanticChallenge` object.
    - *Logic*: Select a target tool, find 2-3 neighbors, and construct a prompt like "Compare X with Y and Z".

### 2. API Integration

#### [MODIFY] [semantic_search_api.py](file:///c:/Users/eqhsp/.gemini/antigravity/playground/ghost-void/toolquest/semantic/semantic_search_api.py)

- Add `POST /api/challenges/generate` endpoint.
- Inject `ChallengeGenerator` dependency.

## Verification Plan

### Automated Tests

- **Cluster Validity**: Verify that `find_tool_clusters` returns tools with similarity > 0.7.
- **Novelty Scoring**: Verify that tools in `user_history` have lower novelty scores.
- **Challenge Structure**: Verify `SemanticChallenge` output matches the schema.

### Manual Verification

- Curl the new endpoint:

  ```bash
  curl -X POST http://localhost:8001/api/challenges/generate \
    -H "Content-Type: application/json" \
    -d '{"target_tool_id": "grep_001", "user_history": ["find_001"]}'
  ```
