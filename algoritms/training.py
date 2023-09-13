# total list of all exersises
import pandas as pd
calf_exercises = {1: "Jumping from a squat.",
                  2: "Block jumps.",
                  3: "Rope jumping.",
                  4: "Jumping up."}
hip_exercises = {1: "Squats.",
                 2: "Barbell lunges.",
                 3: "Back lunge stepping.",
                 4: "Leg raise with expander.",
                 5: "Squatting on one leg.",
                 6: "Split squat."}
exercises_for_the_buttocks = {1: "Glute bridge.",
                              2: "Lunges.",
                              3: "Stepping.",
                              4: "Mahi from a prone position.",
                              5: "Breeding bent legs lying down."}
abdominal_muscle_exercises = {1: "Twisting.",
                              2: "Plank.",
                              3: "Bike."}
lower_back_exercises = {1: "Exercises in the rowing machine.",
                        2: "hyperextension.",
                        3: "Deadlift with dumbbells.",
                        4: "Block pull to the belt while sitting."}
latissimus_dorsi_exercises = {1: "Bent over pull on the block.",
                              2: "Pull-ups.",
                              3: "Vertical pull.",
                              4: "Horizontal pull.",
                              5: "Dumbbell row with support."}
trapezoid_exercises = {1: "Shrugs with free weights.",
                       2: "Shrugs on the block.",
                       3: "Pull to the chin.",
                       4: "Traction to the face with the rise up.",
                       5: "Leading the arm to the side on the block.",
                       6: "Traction of the barbell on the bench to the chest while lying.",
                       7: "Lifting the pancake over your head."}
chest_exercises = {1: "Pushups.",
                   2: "Push-ups on bars.",
                   3: "Bench press.",
                   4: "Breeding dumbbells lying.",
                   5: "Incline dumbbell bench press."}
neck_exercises = {1: "Raising and lowering the shoulders.",
                  2: "Turning the head clockwise.",
                  3: "Head tilt forward-backward, left-right."}
shoulder_exercises = {1: "Army bench press (bench press standing).",
                      2: "Dumbbell bench press sitting or standing.",
                      3: "Pull the bar to the chin (to the chest).",
                      4: "Mahi (breeding) with dumbbells while standing."}
forearm_exercises = {1: "Flexion of the arms at the elbows.",
                     2: "Extension / flexion of the hands.",
                     3: "Scrolling the bar.",
                     4: "Lifting with emphasis.",
                     5: "Expander use."}
triceps_exercises = {1: "Diamond push ups.",
                     2: "Reverse push-ups on the bench.",
                     3: "Push-ups on bars.",
                     4: "Dumbbell bench press from behind the head.",
                     5: "Extension of the arm with a dumbbell in the slope.",
                     6: "Pulling the upper block with ropes.",
                     7: "French press.",
                     8: "Bench press with a narrow grip."}
bicep_exercises = {1: "Lifting the bar for biceps.",
                   2: "Lifting dumbbells for biceps, sitting on an inclined bench.",
                   3: "Lifting dumbbells for biceps with a grip 'Hammer'.",
                   4: "Lifting dumbbells for biceps while standing.",
                   5: "Work in a biceps machine."}


class exersises_for_male_or_male:
    def __init__(self, w_e, m_e):
        self.woman_exercises = w_e
        self.man_exercises = m_e

    def t_es(self):
        print(self.woman_exercises, self.man_exercises)


class type_exersises(exersises_for_male_or_male):
    def __init__(self, weight_less_exersises, muscle_build_exersises):
        super().__init__(weight_less_exersises, muscle_build_exersises)


x = type_exersises("w_e", "m_e")
x.t_es()


your_endurance = {
    'endurance_level': ['beginning', 'advanced', 'master', 'expert'],
    'your_level': [1, 2, 3, 4]
}
myresult = pd.DataFrame(your_endurance, index=[
    'step 1', 'step 2', 'step 3', 'step 4'])

print(myresult.loc['step 4'])

progress_of_beginning = {
    "day 1": {
        "first exercise": "hyperextension. 3/15",
        "second exercise": "Bent over pull on the block. 3/10",
        "thrid exercise": "Pull-ups. 3/5",
        "fourth exercise": "Leading the arm to the side on the block. 3/10"
    },
    "day 2": {
        "first exercise": "Bench press. 3/10",
        "second exercise": "Push-ups on bars. 3/10",
        "thrid exercise": "Lifting the bar for biceps. 2/20",
        "fourth exercise": "Lifting dumbbells for biceps with a grip 'Hammer'. 2/20"
    },
    "day 3": {
        "first exercise": "Jumping up. 3/10",
        "second exercise": "Jumping from a squat. 3/10",
        "thrid exercise": "Squatting on one leg. 3/15",
        "fourth exercise": "Barbell lunges. 3/15"
    }
}
progress_of_advanced = {
    "day 1": {
        "first exercise": "Block pull to the belt while sitting. 3/10",
        "second exercise": "hyperextension. 3/20",
        "thrid exercise": "Dumbbell bench press sitting or standing. 3/15",
        "fourth exercise": "Shrugs on the block. 3/10",
        "fifth exercise": "French press. 3/10"
    },
    "day 2": {
        "first exercise": "Bench press. 3/10",
        "second exercise": "Incline dumbbell bench press. 3/15",
        "thrid exercise": "Work in a biceps machine. 3/15",
        "fourth exercise": "Lifting dumbbells for biceps, sitting on an inclined bench. 3/20",
        "fifth exercise": "Lifting with emphasis. 3/10"
    },
    "day 3": {
        "first exercise": "Plank. 120 second",
        "second exercise": "Jumping up. 3/10",
        "thrid exercise": "Squatting on one leg. 3/15",
        "fourth exercise": "Stepping. 4/20"
    }
}
progress_of_master = {
    "day 1": {
        "first exercise": "hyperextension. 3/25",
        "second exercise": "Exercises in the rowing machine. 3/15",
        "thrid exercise": "Pull to the chin. 3/10",
        "fourth exercise": "Lifting the pancake over your head. 3/15",
        "fifth exercise": "French press. 4/10",
        "sixth exercise": "Extension of the arm with a dumbbell in the slope. 3/15"
    },
    "day 2": {
        "first exercise": "Bench press. 4/10",
        "second exercise": "Incline dumbbell bench press. 3/15",
        "thrid exercise": "Lifting dumbbells for biceps while standing. 3/15",
        "fourth exercise": "Lifting the bar for biceps. 3/15",
        "fifth exercise": "Flexion of the arms at the elbows. 4/10"
    },
    "day 3": {
        "first exercise": "Plank. 180 second",
        "second exercise": "Jumping up. 3/15",
        "thrid exercise": "Leg raise with expander. 4/10",
        "fourth exercise": "Squatting on one leg. 3/15",
        "fifth exercise": "Mahi from a prone position. 4/10"
    }
}
progress_of_expert = {
    "day 1": {
        "first exercise": "hyperextension. 4/25",
        "second exercise": "Exercises in the rowing machine. 3/15",
        "thrid exercise": "Vertical pull. 3/15",
        "fourth exercise": "Horizontal pull. 3/15",
        "fifth exercise": "Dumbbell row with support. 3/15",
        "sixth exercise": "Leading the arm to the side on the block. 3/15"
    },
    "day 2": {
        "first exercise": "Bench press. 4/10",
        "second exercise": "Breeding dumbbells lying. 4/10",
        "thrid exercise": "Incline dumbbell bench press. 4/10",
        "fourth exercise": "Lifting dumbbells for biceps, sitting on an inclined bench. 2/20",
        "fifth exercise": "Lifting dumbbells for biceps with a grip 'Hammer'. 2/20",
        "sixth exercise": "Lifting with emphasis.3/10"
    },
    "day 3": {
        "first exercise": "Plank. 300 second",
        "second exercise": "Jumping up. 3/20",
        "thrid exercise": "Lunges. 4/10",
        "fourth exercise": "Barbell lunges. 3/15",
        "fifth exercise": "Squatting on one leg. 4/10",
        "sixth exercise": "Glute bridge. 3/15"
    }
}

my_set = pd.DataFrame(progress_of_beginning, index=[
    'day 1', 'day 2', 'day 3'])
print(my_set.loc['day 3'])

df = pd.DataFrame(progress_of_beginning)
print(df)

for x in bicep_exercises:
    print(x)

print(triceps_exercises)


class type_o_exersises(type.exersises):
    Title = type.exersises(first_type="muscle building exercises",
                           second_type="weight loss exercises")

    def __str__(self):
        return f'{self.Title}'

    class first_type:
        ex_for_arms = {"forearm_exercises": ["Flexion of the arms at the elbows.",
                                             "Extension / flexion of the hands.",
                                             "Scrolling the bar.",
                                             "Lifting with emphasis.",
                                             "Expander use."]}
        {"bicep_exercises": ["Lifting the bar for biceps.",
                             "Lifting dumbbells for biceps, sitting on an inclined bench.",
                             "Lifting dumbbells for biceps with a grip 'Hammer'.",
                             "Lifting dumbbells for biceps while standing.",
                             "Work in a biceps machine."]}
        {"triceps_exercises": ["Diamond push ups.",
                               "Reverse push-ups on the bench.",
                               "Push-ups on bars.",
                               "Dumbbell bench press from behind the head.",
                               "Extension of the arm with a dumbbell in the slope.",
                               "Pulling the upper block with ropes.",
                               "French press.",
                               "Bench press with a narrow grip."]}
        {"shoulder_exercises": ["Army bench press (bench press standing).",
                                "Dumbbell bench press sitting or standing.",
                                "Pull the bar to the chin (to the chest).",
                                "Mahi (breeding) with dumbbells while standing."]}
        ex_for_legs = {"calf_exercises": ["Jumping from a squat.",
                                          "Block jumps.",
                                          "Rope jumping.",
                                          "Jumping up."]}
        {"hip_exercises": ["Squats.",
                           "Barbell lunges.",
                           "Back lunge stepping.",
                           "Leg raise with expander.",
                           "Squatting on one leg.",
                           "Split squat."]}
        {"exercises_for_the_buttocks": ["Glute bridge.",
                                        "Lunges.",
                                        "Stepping.",
                                        "Mahi from a prone position.",
                                        "Breeding bent legs lying down."]}
        ex_for_body = {"abdominal_muscle_exercises": ["Twisting.",
                                                      "Plank.",
                                                      "Bike."]}
        {"lower_back_exercises": ["Exercises in the rowing machine.",
                                  "hyperextension.",
                                  "Deadlift with dumbbells.",
                                  "Block pull to the belt while sitting."]}
        {"latissimus_dorsi_exercises": ["Bent over pull on the block.",
                                        "Pull-ups.",
                                        "Vertical pull.",
                                        "Horizontal pull.",
                                        "Dumbbell row with support."]}
        {"trapezoid_exercises": ["Shrugs with free weights.",
                                 "Shrugs on the block.",
                                 "Pull to the chin.",
                                 "Traction to the face with the rise up.",
                                 "Leading the arm to the side on the block.",
                                 "Traction of the barbell on the bench to the chest while lying.",
                                 "Lifting the pancake over your head."]}
        {"chest_exercises": ["Pushups.",
                             "Push-ups on bars.",
                             "Bench press.",
                             "Breeding dumbbells lying.",
                             "Incline dumbbell bench press."]}
        {"neck_exercises": ["Raising and lowering the shoulders.",
                            "Turning the head clockwise.",
                            "Head tilt forward-backward, left-right."]}

    class second_type:
        ex_for_legs = {""}
        ex_for_arms = {""}
        ex_for_body = {""}
# print(first_type)
