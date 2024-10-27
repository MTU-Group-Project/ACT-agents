from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from act_agents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class ActAgentsCrew():
	"""ActAgents crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	
	@task
	def research(self) -> Task:
		return Task(
			config=self.tasks_config['research'],
		)

	@agent
	def accountant(self) -> Agent:
		return Agent(
			config=self.agents_config['accountant'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	
	@task
	def calculateRatios(self) -> Task:
		return Task(
			config=self.tasks_config['calculateRatios'],
		)

	@agent
	def recommender(self) -> Agent:
		return Agent(
			config=self.agents_config['recommender'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	
	@task
	def makeRecommendations(self) -> Task:
		return Task(
			config=self.tasks_config['makeRecommendations'],
		)

	@agent
	def blogger(self) -> Agent:
		return Agent(
			config=self.agents_config['blogger'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	
	@task
	def formatOutput(self) -> Task:
		return Task(
			config=self.tasks_config['formatOutput'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ActAgents crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)