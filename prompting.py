from pydantic import BaseModel, Field
from enum import Enum


class Classification(str, Enum):
    achievement = "achievement"
    affection = "affection"
    enjoy_the_moment = "enjoy_the_moment"
    bonding = "bonding"
    leisure = "leisure"
    nature = "nature"
    exercise = "exercise"


class MomentClassification(BaseModel):
    explanation: str = Field(
        description="An explanation of the classification decision."
    )
    classification: Classification


prompt = """You are a system designed to classify written descriptions of happy moments.
I will give you the text of a happy moment, and you should classify it into one of the following categories: {categories}
You will provide an explanation with your decision.

Return your response as JSON according to the following JSON schema:

```
{json_schema}
```

Do not return anything else except your response as JSON. Do not return a JSON schema.
Return an object that follows the schema.

Input: {text}
Output:
"""


text = prompt.format(
    categories=[e.value for e in Classification],
    json_schema=MomentClassification.schema_json(),
    text="I've got my backyard mostly cleaned up and can get to work on some new projects out there.",
).strip()

print(text)
