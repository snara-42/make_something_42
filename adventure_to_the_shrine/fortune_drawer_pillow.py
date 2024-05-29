import random
import time

def draw_fortune():
    fortunes = [
        ("Great Blessing (大吉)", "Great_Blessing.png", """
Debugging: Your efforts in debugging will be exceptionally fruitful. Bugs that have plagued your projects will be swiftly identified and resolved.

System Stability: Your systems will experience remarkable stability. Unexpected crashes and downtime will be minimal.

Innovation: New ideas and innovations will flow easily. Embrace creativity and explore new technologies to enhance your projects.

Collaboration: Collaborate with your team members effectively. Your communication and teamwork will lead to successful outcomes.

Personal Growth: This is a great time for learning and personal development. Consider taking up new courses or certifications to advance your skills.
        """),
        ("Blessing (吉)", "Blessing.png", """
Debugging: Your debugging efforts will be moderately successful. Some bugs will be identified and resolved, but persistent issues may require extra attention and patience.

System Stability: Your systems will generally be stable, though occasional minor issues may arise. Regular maintenance and monitoring will help maintain overall stability.

Innovation: New ideas and innovations will come to you, though they may need refinement and development. Take the time to explore and improve upon them.

Collaboration: Collaboration with your team members will be positive, though occasional miscommunications may occur. Clear communication and understanding will be key to successful teamwork.

Personal Growth: This is a good time for personal development and learning. Consider enhancing your skills through study and practice to achieve steady growth.
        """),
        ("Small Blessing (小吉)", "Small_Blessing.png", """
Debugging: Your debugging efforts will see some success, but progress may be slow. Patience and persistence will be necessary to resolve the more stubborn issues.

System Stability: Your systems will experience occasional instability. Regular checks and prompt responses to minor issues will prevent them from escalating.

Innovation: Innovations and new ideas will come sporadically. You may need to actively seek inspiration and remain open to learning from others.

Collaboration: Team collaboration will be generally positive, though minor conflicts or misunderstandings may arise. Fostering open communication and empathy will help maintain harmony.

Personal Growth: Growth will be steady but gradual. Focus on incremental improvements and continuous learning to build your skills over time.
        """),
        ("Half Blessing (半吉)", "Half_Blessing.png", """
Debugging: Your debugging efforts will yield mixed results. Some issues will be resolved, but others may persist and require creative solutions or external help.

System Stability: Your systems will face some instability. It's important to be vigilant and proactive in monitoring and addressing potential issues before they escalate.

Innovation: Innovations and new ideas will be few and far between. You may need to actively seek out new knowledge and inspiration to spur creativity.

Collaboration: Team collaboration will have ups and downs. Miscommunications and minor disagreements might arise, but with effort, they can be resolved to maintain team cohesion.

Personal Growth: Personal growth will be gradual. Dedicate time to learning and improving your skills, and be patient with the process. Small, consistent efforts will lead to steady progress.
        """),
        ("Future Blessing (末吉)", "Future_Blessing.png", """
Debugging: Challenges in debugging will persist for a while longer. Stay patient and methodical; clarity will come in time.

System Stability: Minor issues may arise, causing brief instability. Regular maintenance and vigilance will be key to minimizing disruptions.

Innovation: Innovation may feel slow, but don't be disheartened. Inspiration will strike when you least expect it. Keep exploring and experimenting.

Collaboration: There may be some misunderstandings with team members. Focus on clear communication and be open to different perspectives to improve teamwork.

Personal Growth: This is a good period to focus on foundational skills. Strengthen your core knowledge and be patient; advanced skills will develop gradually.
        """),
        ("Future Small Blessing (末小吉)", "Future_Small_Blessing.png", """
Debugging: Minor bugs will continue to surface. While they won't be critical, they will require your attention. Stay diligent and thorough in your debugging efforts.

System Stability: Your systems will experience occasional, minor instability. Regular updates and maintenance will help mitigate these issues.

Innovation: Small bursts of creativity will come to you. Capture these moments and use them to incrementally improve your projects.

Collaboration: You may encounter small misunderstandings with team members. Keep communication open and strive for clarity to maintain good teamwork.

Personal Growth: This is a time for steady, gradual improvement. Focus on incremental learning and skill-building. Small steps will lead to significant progress over time.
        """),
        ("Misfortune (凶)", "Misfortune.png", """
Debugging: Significant challenges in debugging will arise. Bugs may be difficult to track down and resolve. Approach problems methodically and seek help if needed.

System Stability: Your systems may experience considerable instability. Prepare for unexpected crashes and downtime. Regular backups and robust error handling will be crucial.

Innovation: Creative blocks may hinder your progress. Take breaks and find inspiration outside of work. New ideas will come in time.

Collaboration: Misunderstandings and conflicts with team members are likely. Focus on clear and empathetic communication. Patience and diplomacy will be essential.

Personal Growth: This period may feel stagnant. Persevere and use this time to reinforce your foundational skills. Growth will come from overcoming these challenges.
        """)
    ]
    return random.choice(fortunes)

def animated_drawing_effect():
    print("Drawing your fortune", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

def main():
    animated_drawing_effect()
    fortune, image_file, description = draw_fortune()
    print(f"Your developer fortune: {fortune}")
    print(description)
    
    # Display the corresponding image
    image_path = f"./images/{image_file}"  # Ensure the images are in an 'images' directory
    try:
        import subprocess
        subprocess.run(["imgcat", image_path])
        return
    except Exception as e:
        print(e)
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            img.show()
        return
    except FileNotFoundError:
        print(f"Image {image_path} not found.")

if __name__ == "__main__":
    main()
