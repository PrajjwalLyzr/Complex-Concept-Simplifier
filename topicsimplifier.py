from lyzr_automata import Task, Agent
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger
from prompts.prompts import agent_prompt, simplified_concept_prompt, image_generation_prompt


def openai_text(ApiKey):
    open_ai_model_text = OpenAIModel(
    api_key= ApiKey,
    parameters={
        "model": "gpt-4o",
        "temperature": 0.5,
        "max_tokens": 1500,
    })

    return open_ai_model_text


def openai_image(ApiKey):
    open_ai_model_image = OpenAIModel(
    api_key= ApiKey,
    parameters={
        "n": 1,
        "model": "dall-e-3",
    })

    return open_ai_model_image

def ComplexTopicSimplifier(apikey, topic, audience):
    concept_clarifier_agent = Agent(
        prompt_persona=agent_prompt(Concept=topic, TargetAudience=audience),
        role="Concept Clarifier",
    )


    concept_clarifier_task = Task(
        name="Concept Topic Simplifier",
        agent=concept_clarifier_agent,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openai_text(ApiKey=apikey),
        instructions=simplified_concept_prompt(Concept=topic, TargetAudience=audience),
        log_output=True,
        enhance_prompt=False,
    )

    logger = Logger()
    
    explanation = LinearSyncPipeline(
        logger=logger,
        name="Complex Topic Simplifier",
        completion_message="Topic Simplified!",
        tasks=[
            concept_clarifier_task
        ],
    ).run()

    return explanation


def VisulaGeneration(apikey, explanation):
    visual_creation_task = Task(
        name="Visual Generation",
        output_type=OutputType.IMAGE,
        input_type=InputType.TEXT,
        model=openai_image(ApiKey=apikey),
        log_output=True,
        instructions=image_generation_prompt(Explationation=explanation)
    )

    logger = Logger()
    
    visual = LinearSyncPipeline(
        logger=logger,
        name="Visual Generation",
        completion_message="Visual Generated!",
        tasks=[
            visual_creation_task
        ],
    ).run()

    return visual

