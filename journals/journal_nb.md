# Journal 

> - **Student**       : _Nathan Bransby_
> - **Filename**      : ```./journal_nb.md```
> - **Github**        : [Nathan-Bransby-NMT](https://github.com/Nathan-Bransby-NMT)
> - **Email Address** : v141198@tafe.wa.edu.au ``TAFE``, [brnsb.eth@mail3.me](https://mail3.me/brnsb.eth) ``Personal``

---

## ``Tuesday 07-05-2024`` _(Summary)_
---

> ### **What work did you do this week?**
> ---
> 
> 1. **Group Assignments**
>   - The class was randomly split into several different groups which will form the teams for the Semester-1 Advanced Programming Project.
>
>     I was assigned into the Team **"Evolve"**, which consists of the following team members: 
>     > - Kinga Papay
>     > - YT (Yang Lim)
>     > - Tendai Chipunzi
>     > - Nathan Bransby (_Myself_)
>
> 2. **Conducted a client meeting to discuss UI/UX design.**
>   - We each conducted individual client meetings to discuss the product we will be developing and to get a better idea on what the issue is and to help understand the accessability & extended functionality provided with video's and IDE/Software for the visually impared.
>     
>   - We then discussed amongst ourselves on what complications we will be tryings to improve and in as well as discuss with our client what features current support works and what features that will assist the visually impaired.
> 
> 3. **Collaboration & Communication**
>   - Set up a team chat to schedule meeting times / days and discuss any updates.
>   - Create a master repository (Github)
>     - Creafe individual branches to work from

> ### **What work you are planning to do next week?**
> ---
> - Set up OpenAI Account and configure API.
> - Fix the file configuration to support Max / Linux users.

> ### Issues and PRs
> ---
> - Unable to run the source files on Mac / Linux OS's.

> ### Retrospective
> - **In what ways have your thoughts about the design changed this week and why?**
>   
>       N/A (First week working on project.)
>   
> - **Did you discuss these ideas with the group? What was the outcome?**
> 
>       Yes we discussed UI/UX design possibilities.
>   
> - **How did you validate your progress this week?**
> 
>       By discussing with the group.

---

## ``Tuesday 14-05-2024`` _(Summary)_
---

> ### **What work did you do this week?**
> ---
> 1. Discussed project progress and any goals that were met over our MS Teams group chat (as i was unwell and did not attend class)

> ### **What work you are planning to do next week?**
> ---
> - Catching up with the team to discuss any changes and proposed solutions with the team.

> ### Issues and PRs
> ---
> - Identified issues trying to run from non Windows OS.

> ### Retrospective
> - **In what ways have your thoughts about the design changed this week and why?**
>   
>       N/A
>   
> - **Did you discuss these ideas with the group? What was the outcome?**
> 
>       N/A
>   
> - **How did you validate your progress this week?**
> 
>       N/A

---

## ``Tuesday 21-05-2024`` _(Summary)_
---

> ### **What work did you do this week?**
> ---
> 1. Discussed UI/UX components
> 2. Colabborated together to come up with use-case scenarios
> 3. Individually designed wire-frame designs on a final appication
> 4. Added our assigned Cert IV students to our MS Teams group chat so they can get involved.
> 5. Discussed with the Cert IV students what is happening with the project.
> 6. Raised low-priority issues on the Repository for the Cert IV students to contribute to.
> 7. Investigate different software for visually impared users to understand how they navigate computer systems.

> ### **What work you are planning to do next week?**
> ---
> * Start making improvements to the existing code base.

> ### Issues and PRs
> ---
> 1. Identified that the button to open text extraction in IDE was not functioning.
> 2. Identified an issue where specific code syntax isn't being identified when being extracted from video.

> ### Retrospective
> - **In what ways have your thoughts about the design changed this week and why?**
>   
>       I now have a better understanding on how a design can be difficult to navigate using software and
>       hardware designed for visually impared users.
>   
> - **Did you discuss these ideas with the group? What was the outcome?**
> 
>       We discussed different user scenarios to develop wireframe designs that cover all stories.
>   
> - **How did you validate your progress this week?**
> 
>       ...

---

## ``Tuesday 28-05-2024`` _(Summary)_
---

> ### **What work did you do this week?**
> ---
> 1. Confirmed new features
> 2. Discussed different methods on reducing the amount of API calls it calls to OpenAI to reduce token expenditure.
> 3. As a group we agreed on the implementation of a pixel averaging feature to pre-process over the video, identifying what frames include an IDE environment to only extract code relevant. Once Identified it will be sent for extraction and the timestamp will be stored in an array to act as a 'bookmark' for the user to cycle through the timestamps, with the extracted code at that time.
> 4. Devided tasks amongst the group to develop solutions for the different stages of our improvement.
> 5. Develop a new file called `analyser.py`, where the code needed for pixel averaging and image conversion will be stored.
> 6. Develop a function [`extract_pixel_average()`], that extracts the pixel average for a `PIL.Image.Image` object and returns a 2D nested list containing the RGB values for the downsampled image.
> 7. Develop a function [`convert_frame_to_pillow_image()`], that takes a capture of a frame and converts it into a `Pillow.Image.Image` object.

> ### **What work you are planning to do next week?**
> ---
> - Continue to work on my video pre-processor, hopefully piecing together the functionality to identify when an IDE is open through pixel averaging.
> - Discuss with the team where they are at, offering assistance where neccessary.

> ### Issues and PRs
> ---
> 1. Identified an issue where the audio `.wav` files are'nt being played when using the 'Mute'/'Un-Mute' button.
> 2. Made fixes on some of the issues raised last week to be more verbose.

> ### Retrospective
> - **In what ways have your thoughts about the design changed this week and why?**
>   
>       Given some confussion arround the wireframe designs, we have decided to go with a more practical
>       function to work on. The design will now implement a navigation pane that allows the user to navigate
>       through extracted code at different timestamps, linking the video to the extracted code. We are also
>       looking to make the application more affordable to make it as accessible as possible for those who are
>       visually impared.
>   
> - **Did you discuss these ideas with the group? What was the outcome?**
> 
>       Yes, we all agreed on minimal changes to the overall design aswell as agreeing on a feature for us all
>       to work towards instead. Once identifying an overall goal, we devided the tasks amongst each other so
>       that we can make a start to develop a final product.
>   
> - **How did you validate your progress this week?**
> 
>       We had a group meeting to discuss our work, and to ensure that we are all happy with the end-design
>       that we are working towards. To ensure that we were making decent progress and to highlight any
>       confusions that we were facing, we included Raf to be part of our group discussion.

---

## ``Tuesday DAY-MONTH-2024`` _(Summary)_
---

> ### **What work did you do this week?**
> ---
> 1. ...

> ### **What work you are planning to do next week?**
> ---
> - ...

> ### Issues and PRs
> ---
> - ...

> ### Retrospective
> - **In what ways have your thoughts about the design changed this week and why?**
>   
>       ...
>   
> - **Did you discuss these ideas with the group? What was the outcome?**
> 
>       ...
>   
> - **How did you validate your progress this week?**
> 
>       ...

---



## Evidence
Mark all that applied for each week

|     Week | Attend class | Respond to PRs/Issues | Met with the team online | Commits to group repo |
|---------:|:------------:|:---------------------:|:------------------------:|:---------------------:|
|`May 7-13` | ☑️ | ❎  <br> **Comment:**<br> <sub><i>- No PRs or Issues to address.</i></sub> | ☑️ | ☑️ |
|`May 14-21`| ❎ <br> **Comment:**<br> <sub><i>- Unwell so didnt attend.</i></sub> | ☑️ | ☑️ | ☑️ |
|`May 21-21`| ☑️ | ☑️ | ☑️ | ☑️ |
|`May 28-21`| ☑️ | ☑️ | ☑️ | ☑️ |
> :warning: If you were not able to mark any of these on a particular week, please email your lecturer with the reason.
