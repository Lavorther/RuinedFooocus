import gradio as gr

from shared import add_ctrl

from random_prompt.build_dynamic_prompt import build_dynamic_prompt

from random_prompt.csv_reader import load_config_csv


insanitylevel = 5
subjects = ["all"]
subjectsubtypesobject = ["all"]
subjectsubtypeshumanoid = ["all"]
subjectsubtypesconcept = ["all"]
artists = [
    "all",
    "all (wild)",
    "none",
    "popular",
    "greg mode",
    "3D",
    "abstract",
    "angular",
    "anime",
    "architecture",
    "art nouveau",
    "art deco",
    "baroque",
    "bauhaus",
    "cartoon",
    "character",
    "children's illustration",
    "cityscape",
    "clean",
    "cloudscape",
    "collage",
    "colorful",
    "comics",
    "cubism",
    "dark",
    "detailed",
    "digital",
    "expressionism",
    "fantasy",
    "fashion",
    "fauvism",
    "figurativism",
    "gore",
    "graffiti",
    "graphic design",
    "high contrast",
    "horror",
    "impressionism",
    "installation",
    "landscape",
    "light",
    "line drawing",
    "low contrast",
    "luminism",
    "magical realism",
    "manga",
    "melanin",
    "messy",
    "monochromatic",
    "nature",
    "nudity",
    "photography",
    "pop art",
    "portrait",
    "primitivism",
    "psychedelic",
    "realism",
    "renaissance",
    "romanticism",
    "scene",
    "sci-fi",
    "sculpture",
    "seascape",
    "space",
    "stained glass",
    "still life",
    "storybook realism",
    "street art",
    "streetscape",
    "surrealism",
    "symbolism",
    "textile",
    "ukiyo-e",
    "vibrant",
    "watercolor",
    "whimsical",
]
imagetypes = [
    "all",
    "all - force multiple",
    "photograph",
    "octane render",
    "digital art",
    "concept art",
    "painting",
    "portrait",
    "anime key visual",
    "only other types",
    "only templates mode",
    "art blaster mode",
    "quality vomit mode",
    "color cannon mode",
    "unique art mode",
    "massive madness mode",
    "photo fantasy mode",
    "subject only mode",
]
promptmode = ["at the back", "in the front"]
promptcompounder = ["1", "2", "3", "4", "5"]
ANDtogglemode = [
    "none",
    "automatic",
    "prefix AND prompt + suffix",
    "prefix + prefix + prompt + suffix",
]
seperatorlist = ["comma", "AND", "BREAK"]
genders = ["all", "male", "female"]

qualitymodelist = ["highest", "gated"]
qualitykeeplist = ["keep used", "keep all"]

generatevehicle = True
generateobject = True
generatefood = True
generatebuilding = True
generatespace = True
generateflora = True
generateanimal = True
generatemanwoman = True
generatemanwomanrelation = True
generatemanwomanmultiple = True
generatefictionalcharacter = True
generatenonfictionalcharacter = True
generatehumanoids = True
generatejob = True
generatefirstnames = True
generatelandscape = True
generateevent = True
generateconcepts = True
generatepoemline = True
generatesongline = True
generatecardname = True
generateepisodetitle = True

config = load_config_csv()

for item in config:
    # objects
    if item[0] == "subject_vehicle" and item[1] != "on":
        generatevehicle = False
    if item[0] == "subject_object" and item[1] != "on":
        generateobject = False
    if item[0] == "subject_food" and item[1] != "on":
        generatefood = False
    if item[0] == "subject_building" and item[1] != "on":
        generatebuilding = False
    if item[0] == "subject_space" and item[1] != "on":
        generatespace = False
    if item[0] == "subject_flora" and item[1] != "on":
        generateflora = False
    # animals
    if item[0] == "subject_animal" and item[1] != "on":
        generateanimal = False
    # humanoids
    if item[0] == "subject_manwoman" and item[1] != "on":
        generatemanwoman = False
    if item[0] == "subject_manwomanrelation" and item[1] != "on":
        generatemanwomanrelation = False
    if item[0] == "subject_manwomanmultiple" and item[1] != "on":
        generatemanwomanmultiple = False
    if item[0] == "subject_fictional" and item[1] != "on":
        generatefictionalcharacter = False
    if item[0] == "subject_nonfictional" and item[1] != "on":
        generatenonfictionalcharacter = False
    if item[0] == "subject_humanoid" and item[1] != "on":
        generatehumanoids = False
    if item[0] == "subject_job" and item[1] != "on":
        generatejob = False
    if item[0] == "subject_firstnames" and item[1] != "on":
        generatefirstnames = False
    # landscape
    if item[0] == "subject_landscape" and item[1] != "on":
        generatelandscape = False
    # concept
    if item[0] == "subject_event" and item[1] != "on":
        generateevent = False
    if item[0] == "subject_concept" and item[1] != "on":
        generateconcepts = False
    if item[0] == "poemline" and item[1] != "on":
        generatepoemline = False
    if item[0] == "songline" and item[1] != "on":
        generatesongline = False
    if item[0] == "subject_cardname" and item[1] != "on":
        generatecardname = False
    if item[0] == "subject_episodetitle" and item[1] != "on":
        generateepisodetitle = False

# build up all subjects we can choose based on the loaded config file
if (
    generatevehicle
    or generateobject
    or generatefood
    or generatebuilding
    or generatespace
):
    subjects.append("object")
if generateanimal:
    subjects.append("animal")
if (
    generatemanwoman
    or generatemanwomanrelation
    or generatefictionalcharacter
    or generatenonfictionalcharacter
    or generatehumanoids
    or generatejob
):
    subjects.append("humanoid")
if generatelandscape:
    subjects.append("landscape")
if (
    generateevent
    or generateconcepts
    or generatepoemline
    or generatesongline
    or generatecardname
    or generateepisodetitle
):
    subjects.append("concept")


# do the same for the subtype subjects
# subjectsubtypesobject = ["all"]
# subjectsubtypeshumanoid = ["all"]
# subjectsubtypesconcept = ["all"]

# objects first
if generateobject:
    subjectsubtypesobject.append("generic objects")
if generatevehicle:
    subjectsubtypesobject.append("vehicles")
if generatefood:
    subjectsubtypesobject.append("food")
if generatebuilding:
    subjectsubtypesobject.append("buildings")
if generatespace:
    subjectsubtypesobject.append("space")
if generateflora:
    subjectsubtypesobject.append("flora")

# humanoids (should I review descriptions??)
if generatemanwoman:
    subjectsubtypeshumanoid.append("generic humans")
if generatemanwomanrelation:
    subjectsubtypeshumanoid.append("generic human relations")
if generatenonfictionalcharacter:
    subjectsubtypeshumanoid.append("celebrities e.a.")
if generatefictionalcharacter:
    subjectsubtypeshumanoid.append("fictional characters")
if generatehumanoids:
    subjectsubtypeshumanoid.append("humanoids")
if generatejob:
    subjectsubtypeshumanoid.append("based on job or title")
if generatefirstnames:
    subjectsubtypeshumanoid.append("based on first name")
if generatemanwomanmultiple:
    subjectsubtypeshumanoid.append("multiple humans")

# concepts
if generateevent:
    subjectsubtypesconcept.append("event")
if generateconcepts:
    subjectsubtypesconcept.append("the X of Y concepts")
if generatepoemline:
    subjectsubtypesconcept.append("lines from poems")
if generatesongline:
    subjectsubtypesconcept.append("lines from songs")
if generatecardname:
    subjectsubtypesconcept.append("names from card based games")
if generateepisodetitle:
    subjectsubtypesconcept.append("episode titles from tv shows")


def ui_onebutton(prompt, run_event):
    def gen_prompt(
        insanitylevel,
        subject,
        artist,
        imagetype,
        antistring,
        prefixprompt,
        suffixprompt,
        givensubject,
        smartsubject,
        giventypeofimage,
        imagemodechance,
        chosengender,
        chosensubjectsubtypeobject,
        chosensubjectsubtypehumanoid,
        chosensubjectsubtypeconcept,
        givenoutfit,
    ):
        prompt = build_dynamic_prompt(
            insanitylevel,
            subject,
            artist,
            imagetype,
            False,
            antistring,
            prefixprompt,
            suffixprompt,
            1,
            "comma",
            givensubject,
            smartsubject,
            giventypeofimage,
            imagemodechance,
            chosengender,
            chosensubjectsubtypeobject,
            chosensubjectsubtypehumanoid,
            chosensubjectsubtypeconcept,
            False,
            False,
            0,
            givenoutfit,
        )

        return prompt 

    def instant_gen_prompt(
        insanitylevel,
        subject,
        artist,
        imagetype,
        antistring,
        prefixprompt,
        suffixprompt,
        givensubject,
        smartsubject,
        giventypeofimage,
        imagemodechance,
        chosengender,
        chosensubjectsubtypeobject,
        chosensubjectsubtypehumanoid,
        chosensubjectsubtypeconcept,
        givenoutfit,
        run_event,
    ):
        prompt = build_dynamic_prompt(
            insanitylevel,
            subject,
            artist,
            imagetype,
            False,
            antistring,
            prefixprompt,
            suffixprompt,
            1,
            "comma",
            givensubject,
            smartsubject,
            giventypeofimage,
            imagemodechance,
            chosengender,
            chosensubjectsubtypeobject,
            chosensubjectsubtypehumanoid,
            chosensubjectsubtypeconcept,
            False,
            False,
            0,
            givenoutfit,
        )

        return prompt, run_event+1

    def add_prompt(
        prompt,
        insanitylevel,
        subject,
        artist,
        imagetype,
        antistring,
        prefixprompt,
        suffixprompt,
        givensubject,
        smartsubject,
        giventypeofimage,
        imagemodechance,
        chosengender,
        chosensubjectsubtypeobject,
        chosensubjectsubtypehumanoid,
        chosensubjectsubtypeconcept,
        givenoutfit,
    ):
        prompt = (
            prompt
            + "---"
            + build_dynamic_prompt(
                insanitylevel,
                subject,
                artist,
                imagetype,
                False,
                antistring,
                prefixprompt,
                suffixprompt,
                1,
                "comma",
                givensubject,
                smartsubject,
                giventypeofimage,
                imagemodechance,
                chosengender,
                chosensubjectsubtypeobject,
                chosensubjectsubtypehumanoid,
                chosensubjectsubtypeconcept,
                False,
                False,
                0,
                givenoutfit,
            )
        )

        return prompt

    with gr.Tab(label="OBP"):
        with gr.Row():
            instant_obp = gr.Button(value="Instant OBP", size="sm", min_width = 1)
            random_button = gr.Button(value="Random Prompt", size="sm", min_width = 1)
            add_random_button = gr.Button(value="+", size="sm", min_width=1)

        with gr.Row():
            assumedirectcontrol = gr.Checkbox(
                label="BYPASS SAFETY PROTOCOLS", value=False
            )
            add_ctrl("obp_assume_direct_control", assumedirectcontrol)

        with gr.Row():
            insanitylevel = gr.Slider(
                1,
                10,
                value=5,
                step=1,
                label="Higher levels increases complexity and randomness of generated prompt",
            )
            add_ctrl("obp_insanitylevel", insanitylevel)
        with gr.Row():
            with gr.Column(scale=1, variant="compact"):
                subject = gr.Dropdown(subjects, label="Subject Types", value="all")
                add_ctrl("obp_subject", subject)
            with gr.Column(scale=1, variant="compact"):
                artist = gr.Dropdown(artists, label="Artists", value="all")
                add_ctrl("obp_artist", artist)

        with gr.Row():
            chosensubjectsubtypeobject = gr.Dropdown(
                subjectsubtypesobject,
                label="Type of object",
                value="all",
                visible=False,
            )
            add_ctrl("obp_chosensubjectsubtypeobject", chosensubjectsubtypeobject)
            chosensubjectsubtypehumanoid = gr.Dropdown(
                subjectsubtypeshumanoid,
                label="Type of humanoids",
                value="all",
                visible=False,
            )
            add_ctrl("obp_chosensubjectsubtypehumanoid", chosensubjectsubtypehumanoid)
            chosensubjectsubtypeconcept = gr.Dropdown(
                subjectsubtypesconcept,
                label="Type of concept",
                value="all",
                visible=False,
            )
            add_ctrl("obp_chosensubjectsubtypeconcept", chosensubjectsubtypeconcept)
            chosengender = gr.Dropdown(
                genders, label="gender", value="all", visible=False
            )
            add_ctrl("obp_chosengender", chosengender)
        with gr.Row():
            with gr.Column(scale=2, variant="compact"):
                imagetype = gr.Dropdown(imagetypes, label="type of image", value="all")
                add_ctrl("obp_imagetype", imagetype)
            with gr.Column(scale=2, variant="compact"):
                imagemodechance = gr.Slider(
                    1,
                    100,
                    value="20",
                    step=1,
                    label="One in X chance to use special image type mode",
                )
                add_ctrl("obp_imagemodechance", imagemodechance)
        with gr.Row():
            gr.Markdown(
                """
                        <font size="2">
                        Override options (choose the related subject type first for better results)
                        </font>
                        """
            )
        with gr.Row():
            givensubject = gr.Textbox(label="Overwrite subject: ", value="")
            add_ctrl("obp_givensubject", givensubject)
            smartsubject = gr.Checkbox(label="Smart subject", value=True)
            add_ctrl("obp_smartsubject", smartsubject)
            givenoutfit = gr.Textbox(label="Overwrite outfit: ", value="")
            add_ctrl("obp_givenoutfit", givenoutfit)
        with gr.Row():
            gr.Markdown(
                """
                        <font size="2">
                        Prompt fields
                        </font>
                        """
            )
        with gr.Row():
            with gr.Column():
                prefixprompt = gr.Textbox(
                    label="Place this in front of generated prompt (prefix)", value=""
                )
                add_ctrl("obp_prefixprompt", prefixprompt)
                suffixprompt = gr.Textbox(
                    label="Place this at back of generated prompt (suffix)", value=""
                )
                add_ctrl("obp_suffixprompt", suffixprompt)
        with gr.Row():
            gr.Markdown(
                """
                        <font size="2">
                        Additional options
                        </font>
                        """
            )
        with gr.Row():
            giventypeofimage = gr.Textbox(label="Overwrite type of image: ", value="")
            add_ctrl("obp_giventypeofimage", giventypeofimage)
        with gr.Row():
            with gr.Column():
                antistring = gr.Textbox(
                    label="Filter out following properties (comma seperated). Example "
                    "film grain, purple, cat"
                    " "
                )
                add_ctrl("obp_antistring", antistring)
        with gr.Row():
            gr.Markdown(
                """
                Proud to be powered by [One Button Prompt](https://github.com/AIrjen/OneButtonPrompt)
                """
            )

        # turn things on and off for gender
        def subjectsvalue(subject):
            enable = subject == "humanoid"
            return {
                chosengender: gr.update(visible=enable),
            }

        subject.change(subjectsvalue, [subject], [chosengender])

        # turn things on and off for subject subtype object
        def subjectsvalueforsubtypeobject(subject):
            enable = subject == "object"
            return {
                chosensubjectsubtypeobject: gr.update(visible=enable),
            }

        subject.change(
            subjectsvalueforsubtypeobject, [subject], [chosensubjectsubtypeobject]
        )

        # turn things on and off for subject subtype humanoid
        def subjectsvalueforsubtypeobject(subject):
            enable = subject == "humanoid"
            return {
                chosensubjectsubtypehumanoid: gr.update(visible=enable),
            }

        subject.change(
            subjectsvalueforsubtypeobject, [subject], [chosensubjectsubtypehumanoid]
        )

        # turn things on and off for subject subtype concept
        def subjectsvalueforsubtypeconcept(subject):
            enable = subject == "concept"
            return {
                chosensubjectsubtypeconcept: gr.update(visible=enable),
            }

        subject.change(
            subjectsvalueforsubtypeconcept, [subject], [chosensubjectsubtypeconcept]
        )

        # turn things on and off for ASSUME DIRECT CONTROL
        def assumedirectcontrolflip(assumedirectcontrol):
            enable = not assumedirectcontrol
            return {
                random_button: gr.update(visible=enable),
                add_random_button: gr.update(visible=enable),
            }

        assumedirectcontrol.change(
            assumedirectcontrolflip,
            [assumedirectcontrol],
            [random_button, add_random_button],
        )

        instant_obp.click(
            instant_gen_prompt,
            inputs=[
                insanitylevel,
                subject,
                artist,
                imagetype,
                antistring,
                prefixprompt,
                suffixprompt,
                givensubject,
                smartsubject,
                giventypeofimage,
                imagemodechance,
                chosengender,
                chosensubjectsubtypeobject,
                chosensubjectsubtypehumanoid,
                chosensubjectsubtypeconcept,
                givenoutfit,
                run_event,
            ],
            outputs=[prompt, run_event],
        )
        random_button.click(
            gen_prompt,
            inputs=[
                insanitylevel,
                subject,
                artist,
                imagetype,
                antistring,
                prefixprompt,
                suffixprompt,
                givensubject,
                smartsubject,
                giventypeofimage,
                imagemodechance,
                chosengender,
                chosensubjectsubtypeobject,
                chosensubjectsubtypehumanoid,
                chosensubjectsubtypeconcept,
                givenoutfit,
            ],
            outputs=[prompt],
        )
        add_random_button.click(
            add_prompt,
            inputs=[
                prompt,
                insanitylevel,
                subject,
                artist,
                imagetype,
                antistring,
                prefixprompt,
                suffixprompt,
                givensubject,
                smartsubject,
                giventypeofimage,
                imagemodechance,
                chosengender,
                chosensubjectsubtypeobject,
                chosensubjectsubtypehumanoid,
                chosensubjectsubtypeconcept,
                givenoutfit,
            ],
            outputs=[prompt],
        )
