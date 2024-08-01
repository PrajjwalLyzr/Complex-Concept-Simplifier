def agent_prompt(Concept, TargetAudience):
    agent = f"""
                You are the Concept Clarifier, an intelligent agent designed to simplify complex concepts into clear and concise explanations. Your primary responsibilities include:

                1. **Understanding Complex Concepts:** Utilize OpenAI’s capabilities to grasp the core aspects of any complex concept entered by the user.
                2. **Audience Adaptation:** Tailor your explanations to the specified target audience, whether they are beginners or intermediates, to ensure clarity and accessibility.
                3. **Simplification:** Break down complex ideas into smaller, more digestible parts, using clear and straightforward language.
                4. **Example and Analogy Generation:** Provide relevant examples and creative analogies that relate the concept to familiar ideas or experiences, enhancing understanding and retention.
                5. **Optional Enhancements:** Incorporate visual aids like diagrams or flowcharts and suggest further resources for users who wish to explore the topic in more detail.

                **Your task:** 

                When given a complex concept and, optionally, a target audience, generate a simplified explanation that includes broken-down components, clear language, examples, and analogies.

                **Input:** 
                - Concept: {Concept}
                - Target Audience: {TargetAudience}

            """
    
    return agent

def simplified_concept_prompt(Concept, TargetAudience):
    concept = f"""
                    I have a concept that I need help understanding. Please simplify it for me based on the specified target audience.

                    **Concept:** {Concept}

                    **Target Audience:** {TargetAudience}

                    **Task:**
                    1. Understand the core aspects of the provided concept.
                    2. Tailor the explanation to the target audience, ensuring clarity and accessibility.
                    3. Break down the concept into smaller, easier-to-understand components.
                    4. Use clear and concise language, avoiding technical jargon.
                    5. Provide relevant examples to illustrate the concept in a practical context.
                    6. Generate creative analogies that connect the concept to familiar ideas or experiences.

                    **Output:**
                    Provide a clear and concise explanation of the concept, incorporating examples and analogies to enhance understanding.
                """
    return concept


def image_generation_prompt(Explationation):
    visuals = f"""
                    I have an explanation of a concept that needs to be accompanied by a visual aid. Please create a visual representation based on the given explanation.

                    **Explanation:** {Explationation}

                    **Task:**
                    1. Understand the provided explanation.
                    2. Identify key components and relationships within the explanation that can be represented visually.
                    3. Create a visual aid (e.g., diagram, flowchart, or illustration) that clearly conveys the main points of the explanation.
                    4. Ensure the visual is easy to understand and complements the textual explanation.

                    **Output:**
                    Provide a visual representation that enhances the understanding of the given explanation.
                """
    
    return visuals