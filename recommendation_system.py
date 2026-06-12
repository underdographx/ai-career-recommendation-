CAREER_DATABASE = [
    {
        "name": "AI Engineer",
        "description": "Build intelligent systems and machine learning models.",
        "skills": ["python", "machine learning", "ai", "deep learning", "data science"]
    },
    {
        "name": "Data Analyst",
        "description": "Analyze data and generate business insights.",
        "skills": ["python", "sql", "excel", "statistics", "visualization"]
    },
    {
        "name": "Frontend Developer",
        "description": "Create user-friendly web interfaces.",
        "skills": ["html", "css", "javascript", "react", "ui"]
    },
    {
        "name": "Backend Developer",
        "description": "Develop APIs and server-side applications.",
        "skills": ["python", "database", "api", "flask", "backend"]
    },
    {
        "name": "Cybersecurity Analyst",
        "description": "Protect systems and networks from threats.",
        "skills": ["cybersecurity", "network security", "ethical hacking", "security"]
    },
    {
        "name": "UI/UX Designer",
        "description": "Design digital experiences and interfaces.",
        "skills": ["figma", "wireframing", "ux", "ui", "prototyping"]
    }
]


def build_user_profile(user_input):
    return [skill.strip().lower() for skill in user_input.split(",")]


def calculate_match(user_skills, career_skills):

    matched_skills = []

    for skill in career_skills:
        if skill in user_skills:
            matched_skills.append(skill)

    score = (len(matched_skills) / len(career_skills)) * 100

    return round(score, 2), matched_skills


def generate_recommendations(user_skills):

    recommendations = []

    for career in CAREER_DATABASE:

        score, matched = calculate_match(
            user_skills,
            career["skills"]
        )

        recommendations.append({
            "career": career["name"],
            "description": career["description"],
            "score": score,
            "matched_skills": matched
        })

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations


def show_recommendations(results):

    print("\n" + "=" * 60)
    print("PERSONALIZED CAREER RECOMMENDATIONS")
    print("=" * 60)

    for rank, item in enumerate(results[:5], start=1):

        print(f"\n{rank}. {item['career']}")
        print(f"Description : {item['description']}")
        print(f"Match Score : {item['score']}%")

        if item["matched_skills"]:
            print("Matched Skills:")
            for skill in item["matched_skills"]:
                print(f"  ✓ {skill}")

        print("-" * 60)


def main():

    print("=" * 60)
    print(" AI Career Recommendation System")
    print("=" * 60)

    print("\nEnter your skills or interests separated by commas.")
    print("Example:")
    print("python, ai, machine learning, data science\n")

    user_input = input("Your Skills: ")

    if not user_input.strip():
        print("No skills entered.")
        return

    user_profile = build_user_profile(user_input)

    recommendations = generate_recommendations(user_profile)

    show_recommendations(recommendations)

    print("\nRecommendation Strategy:")
    print("Skill Matching + Weighted Score Ranking")


if __name__ == "__main__":
    main()