from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    ALLOWED_ARTIFACTS = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact
    }
    
    ALLOWED_COLLECTORS = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }
    
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []
    
    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float,
                          artifact_space: int) -> str:
        
        if artifact_type not in self.ALLOWED_ARTIFACTS:
            raise ValueError("Unknown artifact type!")
        
        searched_artifact = next((artifact for artifact in self.artifacts if artifact.name == artifact_name), None)
        if searched_artifact:
            raise ValueError(f"{artifact_name} has been already registered!")
        
        new_artifact = self.ALLOWED_ARTIFACTS[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."
    
    def register_collector(self, collector_type: str, collector_name: str) -> str:
        if collector_type not in self.ALLOWED_COLLECTORS:
            raise ValueError("Unknown collector type!")
        
        searched_collector = next(
            (collector for collector in self.collectors if collector.name == collector_name), None)
        if searched_collector:
            raise ValueError(f"{collector_name} has been already registered!")
        
        new_collector = self.ALLOWED_COLLECTORS[collector_type](collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."
    
    def perform_purchase(self, collector_name: str, artifact_name: str) -> str:
        searched_collector = next(
            (collector for collector in self.collectors if collector.name == collector_name), None)
        if searched_collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        
        searched_artifact = next((artifact for artifact in self.artifacts if artifact.name == artifact_name), None)
        if searched_artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        
        if not searched_collector.can_purchase(searched_artifact.price, searched_artifact.space_required):
            return "Purchase is impossible."
        
        self.artifacts.remove(searched_artifact)
        searched_collector.purchased_artifacts.append(searched_artifact)
        searched_collector.available_money -= searched_artifact.price
        searched_collector.available_space -= searched_artifact.space_required
        
        return f"{collector_name} purchased {artifact_name} for a price of {searched_artifact.price:.2f}."
    
    def remove_artifact(self, artifact_name: str) -> str:
        searched_artifact = next((artifact for artifact in self.artifacts if artifact.name == artifact_name), None)
        if searched_artifact is None:
            return "No such artifact."
        
        self.artifacts.remove(searched_artifact)
        return (f"Removed {searched_artifact.artifact_information()}")
    
    def fundraising_campaigns(self, max_money: float) -> str:
        counter = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                counter += 1
        
        return f"{counter} collector/s increased their available money."
    
    def get_auction_report(self) -> str:
        sorted_collectors = sorted(self.collectors,
                                   key=lambda collector: (-len(collector.purchased_artifacts), collector.name))
        
        available_artifacts = len(self.artifacts)
        total_bought_artifacts = 0
        output_collectors: list[str] = []
        for collector in sorted_collectors:
            total_bought_artifacts += len(collector.purchased_artifacts)
            output_collectors.append(str(collector))
        
        result: list[str] = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {total_bought_artifacts}",
            f"Available artifacts for sale: {available_artifacts}",
            "***"
        ]
        
        result.extend(output_collectors)
        return "\n".join(result)
