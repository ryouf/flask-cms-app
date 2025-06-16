# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

I selected Azure App Service as the deployment method due to its cost-effectiveness compared to a virtual machine. Unlike VMs, which often require more setup, updates, and security handling, App Services offer a simpler and faster deployment process. The platform fits my workflow well—especially with how quickly I can push changes from GitHub directly to the web app.
In terms of availability and performance, App Services seem more reliable and efficient for a lightweight CMS like this. If my project were hosted on a VM, I'd likely need to handle reboots, OS patching, and scaling manually. The App Service model allows me to scale when needed with minimal configuration overhead. Considering the balance between cost, performance, and ease of use, App Service was the right fit for this project.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If future requirements involve using very customized templates or advanced features not supported by App Services, I might reconsider using a virtual machine. VMs give you more control over the environment, which can be helpful for unique configurations or third-party integrations. However, unless those needs arise, I expect to continue with App Service since it supports automated deployments and suits agile development well.offerings that streamline changes and deployments from a GitHub repo or other sources. A virtual machine takes a lot of thoughtful planning and work to make it secure and up-to-date, so I do not see this changing in the near future. 