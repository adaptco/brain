# VT-TQ-Search: ToolQuest Semantic Tool Finder

## Goal

Extend ToolQuest Pro with semantic search for tools, transforming tool discovery into an active game mechanic while providing real utility for developers.

## Strategic Rationale

- **Preserves Core**: Builds on existing ToolQuest Pro gameplay kernel
- **Maximizes Reuse**: Work orders become training data for embeddings
- **Clean Vector Space**: Adds one semantic dimension instead of fragmenting across multiple apps
- **Immediate Value**: Practical tool discovery + gamified learning

## Architecture

### Vector-Token Axes

1. **search_mode**: keyword → **semantic** (embed task descriptions, tool names, error messages)
2. **integration**: passive lookup → **active game mechanic** (finding the right tool = challenge)

### Data Schema

```typescript
interface ToolEmbedding {
  tool_id: string;
  tool_name: string;
  description: string;
  category: string[];
  usage_examples: string[];
  error_patterns: string[];
  embedding_vector: number[]; // 768-dim from sentence-transformers
  popularity_score: number;
  difficulty_tier: 1 | 2 | 3 | 4 | 5;
}

interface WorkOrderEmbedding {
  order_id: string;
  task_description: string;
  required_tools: string[];
  common_errors: string[];
  embedding_vector: number[];
  completion_rate: number;
  avg_time_seconds: number;
}

interface SemanticChallenge {
  challenge_id: string;
  generated_task: string;
  semantic_neighbors: string[]; // Similar tool IDs
  difficulty_score: number;
  xp_reward: number;
  time_limit_seconds: number;
}
```

## Proposed Changes

### [NEW] `toolquest/semantic/`

#### [NEW] `embedding_pipeline.py`

- Embed tool names, descriptions, usage examples
- Embed work order task descriptions and error patterns
- Use `sentence-transformers/all-mpnet-base-v2` for consistency
- Store in Qdrant collection `toolquest_tools`

#### [NEW] `semantic_search_api.py`

- FastAPI endpoint: `POST /api/semantic/search`
- Input: natural language query (e.g., "find files recursively")
- Output: ranked list of tools with similarity scores
- Filters: category, difficulty, popularity

#### [NEW] `challenge_generator.py`

- Query vector DB for similar work orders
- Mutate task descriptions (change context, tool set, constraints)
- Assign difficulty based on semantic distance from known patterns
- Generate XP rewards proportional to novelty

### [MODIFY] `toolquest_pro_multiplayer.tsx`

#### Discovery Mode UI

```tsx
<DiscoveryMode>
  <SemanticSearchBar 
    placeholder="Describe what you want to do..."
    onSearch={handleSemanticSearch}
  />
  <ToolResults>
    {results.map(tool => (
      <ToolCard 
        key={tool.id}
        name={tool.name}
        similarity={tool.score}
        difficulty={tool.tier}
        onSelect={() => startChallenge(tool)}
      />
    ))}
  </ToolResults>
  <AIGeneratedChallenges>
    {challenges.map(c => (
      <ChallengeCard
        task={c.generated_task}
        xp={c.xp_reward}
        timeLimit={c.time_limit_seconds}
      />
    ))}
  </AIGeneratedChallenges>
</DiscoveryMode>
```

#### Leaderboard Extension

- Add "Semantic Explorer" rank (XP from AI-generated challenges)
- Track "Discovery Score" (unique tools found via semantic search)

### [NEW] `toolquest/semantic/docker-compose.yml`

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
  
  embedding-worker:
    build: ./embedding_pipeline
    environment:
      QDRANT_HOST: qdrant
      MODEL_ID: sentence-transformers/all-mpnet-base-v2
  
  semantic-api:
    build: ./semantic_search_api
    ports:
      - "8001:8000"
    environment:
      QDRANT_HOST: qdrant
```

## Embedding Strategy

### Training Data Sources

1. **Tool Metadata**: Names, descriptions, man pages
2. **Work Orders**: Task descriptions from existing gameplay
3. **Error Logs**: Common failure patterns and solutions
4. **User Queries**: Anonymized search history (if available)

### Embedding Model

- **Primary**: `sentence-transformers/all-mpnet-base-v2` (768-dim)
- **Fallback**: `all-MiniLM-L6-v2` (384-dim, faster inference)

### Indexing Pipeline

1. Parse tool metadata from package managers (npm, pip, cargo)
2. Normalize text (NFKC, lowercase, remove special chars)
3. Generate embeddings in batches (32 tools/batch)
4. Upsert to Qdrant with metadata filters

## Gameplay Integration

### Discovery Mode Flow

1. Player enters natural language query
2. System retrieves top-K semantically similar tools
3. Player selects a tool to "unlock" (costs in-game currency)
4. System generates AI challenge using that tool
5. Player completes challenge → earns XP + tool mastery

### AI Challenge Generation

```python
def generate_challenge(base_order: WorkOrder, difficulty: int) -> Challenge:
    # Retrieve semantic neighbors
    neighbors = qdrant.search(base_order.embedding, limit=5)
    
    # Mutate task description
    mutations = [
        "change file type",
        "add time constraint",
        "increase data volume",
        "introduce error condition"
    ]
    
    mutated_task = apply_mutation(base_order.task, mutations[difficulty-1])
    
    # Compute XP reward
    xp = base_xp * (1 + semantic_distance * novelty_factor)
    
    return Challenge(
        task=mutated_task,
        required_tools=select_tools_from_neighbors(neighbors),
        xp_reward=xp,
        time_limit=estimate_time(difficulty)
    )
```

## Verification Plan

### Phase 1: Embedding Quality

- Embed 100 sample tools
- Manual review of top-5 semantic neighbors
- Assert: `grep` neighbors include `rg`, `ag`, `ack`

### Phase 2: Search Accuracy

- Query: "find large files"
- Expected results: `find`, `du`, `fd`, `ncdu`
- Measure: Precision@5, Recall@10

### Phase 3: Challenge Viability

- Generate 10 AI challenges
- Human playtest for clarity and difficulty
- Adjust mutation logic based on feedback

### Phase 4: Gameplay Integration

- A/B test: Discovery Mode vs traditional work orders
- Metrics: engagement time, XP earned, tool diversity

## Success Criteria

- ✅ Semantic search returns relevant tools for 90%+ of queries
- ✅ AI-generated challenges are completable and rated "fair" by players
- ✅ Discovery Mode increases tool diversity by 30%+
- ✅ Players spend 20%+ of session time in Discovery Mode
