from src.explainability.explanation_generator import (
    generate_explanation
)

print(

    generate_explanation(

        semantic_score=85,

        career_fit_score=90,

        product_score=40

    )

)