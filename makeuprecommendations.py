# if unsure start shape quiz function
def face_shape_quiz():
    print("I see you do not know your face shape.\nLet's determine your face shape with this quick quiz:")
    
    # Question 1
    q1 = input("Is your face longer than it is wide? (yes/no): ").lower()

    if q1 == "yes":
        # Question 2 
        q2 = input("Is your forehead slightly wider than your jawline? (yes/no): ").lower()
        if q2 == "yes":
            return "Oval Face"
        else:
            # Question 3 
            q3 = input("Are your cheekbones the widest part of your face? (yes/no): ").lower()
            if q3 == "yes":
                return "Diamond Face"
            else:
                return "Unfortunately, we cannot currently determine your face shape."
    else:
        # Question 4 
        q4 = input("Is your jawline strong and angular? (yes/no): ").lower()
        if q4 == "yes":
            return "Square Face"
        else:
            # Question 5 
            q5 = input("Is your face soft with rounded cheeks and no sharp angles? (yes/no): ").lower()
            if q5 == "yes":
                return "Round Face"
            else:
                return "Unfortunately, we cannot currently determine your face shape."


def makeup_recommendations():
    def round_face():
        return """
        Choose a lightweight foundation that matches your shade. Do not apply a second layer, as it might make your face look rounder.
        Apply concealer under the eyes in an upward motion, on the bridge of the nose, chin, top of the lip, and forehead. Let it sit for 2 minutes.
        While the concealer sets, apply contour that is 1-2 shades darker than your skin tone. Contour below your cheekbones, the sides of your forehead, and along your jawline to give a snatched look. Blend out the contour.
        Blend the concealer upwards. Avoid blending downwards, as we want to create a slimmer illusion.
        Add a sharp line of concealer below your contour on your cheekbones and blend it out.
        Apply cream blush directly above your contour and blend it. Swipe the blush slightly higher on your cheekbones to lift the face.
        Once you're done, set your face with setting spray and let it dry.
        Apply pressed powder where you applied concealer.
        Set the rest of your face with powder where you applied foundation.
        Add powder blush over your cream blush and blend it.
        Set with setting spray again.
        You are done!
        """
    
    def oval_face():
        return """
        Choose a lightweight foundation that matches your shade. Apply an even layer for a smooth base.
        Apply concealer under the eyes, on the bridge of the nose, chin, and forehead. Let it sit for 2 minutes.
        Apply contour that is 1-2 shades darker than your skin tone. Contour lightly below your cheekbones, along the sides of your forehead, and under your jawline to define your natural structure. Blend well.
        Blend the concealer upwards, especially under the eyes, to lift the face.
        Apply cream blush to the apples of your cheeks, blending it upwards toward your temples for a natural lift.
        Set your face with setting spray and let it dry.
        Apply pressed powder where you applied concealer to set it in place.
        Set the rest of your face with powder where you applied foundation.
        Add powder blush over your cream blush and blend.
        Set your face again with setting spray.
        You are done!
        """
    
    def square_face():
        return """
        Choose a lightweight foundation that matches your shade and apply evenly to create a smooth base.
        Apply concealer under your eyes, on the bridge of your nose, chin, and center of the forehead. Let it sit for 2 minutes.
        Apply contour that is 1-2 shades darker than your skin tone. Focus on contouring the sides of your forehead, below your cheekbones, and along your jawline to soften the angles of your face. Blend thoroughly.
        Blend the concealer upwards under the eyes and softly on the forehead to create balance.
        Apply cream blush to the apples of your cheeks, blending it slightly upward and toward the temples to soften the face shape.
        Set your makeup with setting spray and allow it to dry.
        Apply pressed powder to the areas where you applied concealer to set it.
        Set the rest of your face with powder where you applied foundation.
        Apply powder blush over your cream blush and blend it out.
        Set with setting spray once again.
        You are done!
        """
    
    def diamond_face():
        return """
        Choose a lightweight foundation that matches your shade and apply it evenly for a smooth, natural finish.
        Apply concealer under the eyes, on the center of your forehead, bridge of the nose, chin, and below the cheekbones. Let it sit for 2 minutes.
        Apply contour that is 1-2 shades darker than your skin tone. Focus on below your cheekbones to define them, and a little on the forehead and jawline to balance the width of the cheekbones. Blend well.
        Blend the concealer upwards under your eyes and softly across your forehead and chin to soften sharp angles and highlight the center of your face.
        Apply cream blush to the tops of your cheekbones, blending upward toward your temples to lift the face without adding width to the cheeks.
        Set your makeup with setting spray and allow it to dry.
        Apply pressed powder where you placed concealer to set it.
        Set the rest of your face with powder on areas where you applied foundation.
        Apply powder blush over the cream blush and blend well.
        Set your face again with setting spray to finish.
        """
    
    recommendation = {
        "Round": round_face(),
        "Oval": oval_face(),
        "Square": square_face(),
        "Diamond": diamond_face()
    }

    name = input("What is your name? ")
    print(f"Welcome, {name}!")
    print("Today we are going to recommend makeup products for you based on your face type and preferences.")
    
    face_shape = input("What would you consider the shape of your face? (Oval, Round, Square, Diamond)?: ").capitalize()
    
    if face_shape.lower() in ["i do not know", "don't know", "no idea"]:
        face_shape = face_shape_quiz()
    
    if "Unfortunately" in face_shape:
        print(face_shape)  
        return
    
    face_shape = face_shape.capitalize()  

    if face_shape in recommendation:
        print(recommendation[face_shape])
    else:
        print("Sorry, I don't have recommendations for that face shape.")


makeup_recommendations()
