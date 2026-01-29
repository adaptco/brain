# Task: Batch Processing and Sovereign OS Integration

- [x] Implement Batch Processing for Embed Worker
  - [x] Modify `docling_worker` to enqueue batches
  - [x] Modify `embed_worker` to use `DataLoader` logic

- [x] Fix markdown warnings in `GEMINI.md`
- [x] Debug persistent C++ include errors in `src/main.cpp`
- [ ] Deploy `docling-cluster` (Pending Docker)

# Task: VT-TQ-Search Enhancements

- [x] Implement `ChallengeGenerator` logic
  - [x] Create `toolquest/semantic/challenge_generator.py`
  - [x] Implement semantic neighbor retrieval
  - [x] Implement prompt generation logic
- [x] Integrate Challenge Generation into API
  - [x] Add `POST /api/challenges/generate` endpoint
