class PromptEvaluator:

    ROLE_KEYWORDS = [
        "you are",
        "act as",
        "behave as",
        "assistant",
        "expert",
        "coach",
        "reviewer"
    ]

    CONTEXT_KEYWORDS = [
        "context",
        "background",
        "given",
        "based on",
        "document",
        "input",
        "user",
        "following"
    ]

    SPECIFIC_KEYWORDS = [
        "step by step",
        "exactly",
        "only",
        "must",
        "should",
        "format",
        "json",
        "bullet",
        "table",
        "explain",
        "summarize",
        "translate",
        "review"
    ]

    @classmethod
    def evaluate(cls, prompt: str) -> dict:

        prompt_lower = prompt.lower()

        role_score = sum(
            keyword in prompt_lower
            for keyword in cls.ROLE_KEYWORDS
        )

        context_score = sum(
            keyword in prompt_lower
            for keyword in cls.CONTEXT_KEYWORDS
        )

        specificity_score = sum(
            keyword in prompt_lower
            for keyword in cls.SPECIFIC_KEYWORDS
        )

        total_score = (
            role_score +
            context_score +
            specificity_score
        )

        return {
            "Role Score": role_score,
            "Context Score": context_score,
            "Specificity Score": specificity_score,
            "Total Score": total_score
        }

    @classmethod
    def compare(cls, prompt1: str, prompt2: str):

        score1 = cls.evaluate(prompt1)
        score2 = cls.evaluate(prompt2)

        print("=" * 60)

        print("Prompt 1")
        print(score1)

        print()

        print("Prompt 2")
        print(score2)

        print()

        if score1["Specificity Score"] > score2["Specificity Score"]:
            print("✔ Prompt 1 is more specific")
        elif score2["Specificity Score"] > score1["Specificity Score"]:
            print("✔ Prompt 2 is more specific")
        else:
            print("✔ Both prompts are equally specific")

        print()

        if score1["Role Score"] > score2["Role Score"]:
            print("✔ Prompt 1 has a better defined role")
        elif score2["Role Score"] > score1["Role Score"]:
            print("✔ Prompt 2 has a better defined role")
        else:
            print("✔ Both prompts define the role equally")

        print()

        if score1["Context Score"] > score2["Context Score"]:
            print("✔ Prompt 1 provides better context")
        elif score2["Context Score"] > score1["Context Score"]:
            print("✔ Prompt 2 provides better context")
        else:
            print("✔ Both prompts provide similar context")