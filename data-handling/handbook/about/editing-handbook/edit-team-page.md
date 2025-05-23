---
title: "Edit your team page entry"
description: "Instructions on how to add yourself to the team page, and make edits."
---

This page specifically covers how to add yourself to the team page, add your pets to the pets page, and edit the relevant entries.

For the handbook, see the [editing handbook page](/handbook/about/editing-handbook/).

## Add yourself to the Team Page

We are happy to have you join our company and to include you in the team pages found on [our website](https://about.gitlab.com/company/team/) and [in the handbook](/handbook/company/team/)! [A sync](/handbook/people-group/engineering/onboarding/#sync-to-team-page) will add a basic entry for you on your third day of employment at GitLab. You are invited to personalize this entry and add more information to it. If an update is not properly reflected, verify that your Workday setting is correct. The same file is referenced for both team pages, however some of the fields that display are different. All of the available fields are documented in the [team member data schema](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/team_members/person/README.md).

Ask anyone in the company for help if you need it, including the `#mr-buddies` Slack channel. There are **three** ways to update the website:

1. [Add your info on GitLab.com using the Web IDE](#method-1-add-your-info-on-gitlabcom-using-web-ide) (recommended)
1. [Add your info on GitLab.com using the 'web interface'](#method-2-add-your-info-on-gitlabcom-using-the-web-interface)
1. [Add your info using a Local Git clone (using the terminal and an IDE)](#method-3-add-your-info-using-a-local-git-clone-using-the-terminal-and-an-ide)

Choose the method below that feels most comfortable and have the following information handy:

- Name of the People Connect Team member helping you with onboarding.
<a name="picture-requirements"></a>
- A picture of yourself for the team page
  > **Picture Requirements**
  >
  > - Crop image to a perfect square.
  > - Maximum dimension is 400 by 400 pixels.
  > - Use the JPEG (`.jpg`) or PNG (`.png`) format.
  > - Keep the file size below 100k. Minify using something like [tinyjpg.com](https://tinyjpg.com/).
  > - Test image in color and black-and-white (you will add the color version).
  > - Name file `yournameinlowercase` with the appropriate file extension.
- Story about your background and interests. (See other team member profiles for examples.)
- Add your personal LinkedIn / Twitter / GitLab handles. When adding these handles, make sure to only include your username without any links or `@` in front of them, such as `LinkedIn: username`. (Some incorrect examples are: `LinkedIn: linkedin.com/in/username`, `LinkedIn: @username`.)
- A relative link to your role. If your link is `https://handbook.gitlab.com/job-families/engineering/support-engineer/` use `/job-families/engineering/support-engineer/`. Refer to other entries for reference.

{{% alert title="Note" color="primary" %}}
For more information on setting the `Export Name/Location to Team Page?` opt-in mentioned below, search for the ["How to: Set Team Page Export Preferences" Google doc](https://drive.google.com/drive/search?q=how+to+Set+Team+Page+Export+Preferences) (internal).
{{% /alert %}}

### Method 1: Add your info on GitLab.com using Web IDE

1. Go to the [Handbook version of the team page](/handbook/company/team/) and find yourself.
   - Note: if you chose `No` in Workday for `Export Name/Location to Team Page?`, you will have to find yourself by your job title instead of your name. In this case, some changes like `name` will be overwritten by the sync.
1. Click on the avatar above your name (or job title). A modal will open.
1. In that modal, on the bottom, click the `Edit this page` button.
1. Our web editor will open with your team page entry opened.
1. Update your details:
   - Update your `name` if needed to your `FirstName LastName`or `PreferredName LastName`
   - `locality` should be left empty
   - `country` should be set to `Remote`
   - Verify your `role`
   - If your position title is incorrect or not filled in, navigate to `job_families.yml` and use `command-F` (macOS) or `ctrl-F` (nix) to search for your job title. You can search for files in the Web IDE using `command-P` (macOS) or `ctrl-P` (nix).
   - Check that your role has a link to your job description. If not, add a link. For example, change `<a href="">Solutions Architect</a>` to `<a href="/job-families/sales/solutions-architect/">Solutions Architect</a>`.
   - Verify `reports_to` lists your manager using the `slug` value from their team page entry. The filename (without the extension) is also the slug, meaning `aname.yml` has a slug of `aname`.
   - If you are a manager, verify the `reports_to` of your direct reports are referring to your `slug`.
   - If you're currently on a borrow request, add `borrow` and set the `to` and `end_date` keys, such as:

     ```yaml
     borrow:
       to: ramya-authappan
       end_date: 2023-09-15
     ```

   - Set your current work priorities in the `work_priorities` field, as an array, such as:

     ```yaml
     work_priorities:
       - Product Analytics
       - ModelOps
     ```

   - Add the filename of your profile picture, making sure to match letter case. Delete `../gitlab-logo-extra-whitespace.png`, if present. The completed line should look like this: `picture: yournameinlowercase.jpg`.
   - Add your pronouns.
   - Consider adding `pronunciation` for your full name to help others to pronounce your name correctly (such as, `Sid See-brandy` for Sid Sijbrandij).
   - Add your Twitter and GitLab handles without the leading `@`.
   - Add your Mastodon account in the format `mastodon.instance/@username`. Basically, the profile link without the `https://`.
   - Ensure your list of `departments` is accurate. Use other team members' as a reference.
   - Add your [`specialty`](/handbook/company/structure/#specialist).
   - Add your [`expertise`](/handbook/company/structure/#expert). This must be formatted as HTML. An array will display incorrectly.
   - Add your own `story`. Use other team members' stories as a reference.
   - If remote work has [changed your life](/handbook/company/culture/all-remote/people/) in a meaningful way, consider adding your own `remote_story`, using other team members' remote stories as a [reference](https://gitlab.com/gitlab-com/marketing/corporate_marketing/corporate-marketing/uploads/8161ceac4523a9f36244f9533960ccbd/remote-story-example.png)
   - Update any data that was filled in but is incorrect.

     **Important:** Do not use the `tab` character, and respect the spaces between lines to avoid breaking the page format. Referenced file names/extensions are case sensitive, and a file that is not found will cause a pipeline failure. The file should end with an empty newline or it will cause a pipeline failure.
1. To upload your image, ensure that it is prepared according to the [Picture Requirements](#picture-requirements).
   1. Navigate to find the `team` folder using the path `sites/uncategorized/source/images/team/`. To do this, you must first notice in the left (by default) file tree that you are in a file that is within the `person` folder, which is within the `team_members` folder, which is within the `data` folder. You can close folders by clicking on the ⋁ to the left of the folder name. Once you have closed the `data` folder, you will see the `sites` folder, 6 folders down. Open `sites` by clicking the >, then `uncategorized`, then `source`, then `images`, and finally `team`.
   1. Right click on `team` folder, and choose `Upload`.
   1. Select the image you want to upload, and `Open`.
   1. If the image filename is different from what you updated your team page file previous, you need navigate back to your team page entry. You can do this by either closing the `sites` folder and opening `data`, then `team members`, `person`, and the folder containing you file; or you can notice your file tab on the top bar, and you can click on it to be taken to that file.
   1. If you did the previous step, update your `picture` field to your filename. Delete the content that is this line after the `picture:` that starts with `../gitlab` etc. Make sure to match the letter case of your picture file. The completed line should look like this: `picture: yournameinlowercase.jpg` for example.
1. Once you have finished, click the `Source Control` icon on the left. It should have a small circle with a number inside of it. See point 5 of [Using the new Web IDE to edit the handbook](/handbook/about/editing-handbook/#use-the-web-ide-to-edit-the-handbook) for details.
1. Add a short description of your changes in the box above the `Commit and push` button. An example description would be `Update details to my team page entry`.
1. Click the ⋁ on the right side of the `Commit and push` button.
1. Choose the `Create new branch and commit` option.
1. You will then be in the `Create a new branch name and commit` field. Enter your branch name, in the format of `yourinitials-add-YOURNAME-to-team-page-date` or similar. Example: `plh-add-paulalilyherbert-to-team-page-feb06` and press `Return/Enter`.
1. Look for a pop-up in the bottom right, and click on `Create MR`. If this message disappears, click on the notification bell icon on the bottom right, and it will bring back the message.
1. Once on the `Create a new merge request` page, in the `Description` box, under the `Why is this change being made?` heading, explain what changes are being made and why. For this specific MR, you can enter something like: `Adding my information and picture to the team page as part of onboarding tasks.` For this MR, you do not need to change anything else in the description text.
1. Scroll down and `Create merge request`.
1. Review the Author Checklist in the description, and check off all applicable tasks.
1. Add your People Connect onboarding team member and Manager as Reviewers. On the right side, you'll see a section for reviewers, and you can add them by editing the list and searching for their names or usernames.
1. Once they have reviewed and do not request any changes, they should approve and merge the MR.

### Method 2: Add your info on GitLab.com using the 'web interface'

1. Go to the [GitLab.com / www-gitlab-com](https://gitlab.com/gitlab-com/www-gitlab-com/) project.
1. Click the `+` under the red line near the top of the screen.
1. Click `New branch`.
1. For `Branch name`, name it something unique (it's temporary so don't worry too much about the exact name) like *your initials-team-page-update-yourdepartment-the date* and click `Create branch`. Example: `hk-team-page-update-custsupport-feb06`
1. Start by adding your image. Click on `Repository` on the left side.
1. In the file browser, navigate to `sites/uncategorized/source/images/team`.
1. At the top of the page click `+` and choose `Upload file` to upload your picture. Be sure to follow the [picture requirements](#picture-requirements). Add a commit message in the format *Add YourFirstName YourLastName to team page*. Ensure the target branch is the one you previously created. Turn off the `Start a new merge request with these changes` toggle. Click `Upload file`.
1. Now you will edit your biographical information. All the bio information displayed on the Team page is pulled from a data file. Navigate to `data/team_members/persondata/FIRST_LETTER_OF_YOUR_FIRST_NAME/SLUG_REPLACE.yml` (you are looking for a file that specifies your name or slug).
1. Navigate to the relevant `yourslug.yml` file. Click on `Edit` on the top right side of your screen, and choose `Edit single file`.
1. See point 5 in the above [Method 1: Add your info on GitLab.com using Web IDE](#method-1-add-your-info-on-gitlabcom-using-web-ide) for the list of fields and how to fill them in.
1. After you add your information, add a commit message, and click on "Commit Changes". If you have the "create a new merge request" option checked, then it will create the merge request (MR) for you.
1. Now [Create a merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html) in [GitLab.com](https://gitlab.com/gitlab-com/www-gitlab-com) with the branch that you created by clicking `Create merge request` button.
1. Once on the `Create a new merge request` page, in the `Description` box, under the `Why is this change being made?` heading, explain what changes are being made and why. For this specific MR, you can enter something like: `Adding my information and picture to the team page as part of onboarding tasks.` For this MR, you do not need to change anything else in the description text.
1. Click `Create merge request`.
1. At the upper right of the new page, click `edit` next to `Reviewer`. Set your People Connect onboarding team member and your manager as reviewer for this merge request.

### Method 3: Add your info using a Local Git clone (using the terminal and an IDE)

*Note:* This method may take longer than other methods, because it requires `git clone` for a large repository.

1. Download Git, following the [start using git documentation](https://docs.gitlab.com/ee/topics/git/how_to_install_git/).
1. Follow the steps to create and add your [SSH keys](https://docs.gitlab.com/ee/user/ssh.html).
1. Clone the [www-gitlab-com project](https://gitlab.com/gitlab-com/www-gitlab-com) through your terminal, following the [command line commands documentation](https://docs.gitlab.com/ee/topics/git/commands.html#git-clone).
1. [Create and checkout a new branch](https://docs.gitlab.com/ee/topics/git/branch.html) for the changes you will be making.
1. Add your picture to the `sites/uncategorized/source/images/team/` directory. Be sure to follow the [picture requirements](#picture-requirements).
1. Open `data/team_members/person/FIRST_LETTER_OF_YOUR_FIRST_NAME/SLUG_REPLACE.yml` in your favorite editor, specifically looking for the file with your name or slug.
1. See point 5 in the above [Method 1: Add your info on GitLab.com using Web IDE](#method-1-add-your-info-on-gitlabcom-using-web-ide) for the list of fields and how to fill them in.
1. Save the changes to the file in `data/team_members/person/FIRST_LETTER_OF_YOUR_FIRST_NAME/` that you just edited.
1. Optionally, to see your changes locally:
   1. Manually run a command to compile the changes you just made into a file that actually populates the team page:

      ```bash
      cd <WWW-GITLAB-COM REPO ROOT>
      bundle exec rake build:team_yml
      ```

   1. Start a middleman development server in the `uncategorized` site:

      ```bash
      cd sites/uncategorized
      NO_CONTRACTS=true bundle exec middleman
      ```

   1. Open the team page and search for your name `http://localhost:4567/company/team`
      *Note:* Searching the handbook in your local environment yields production results, so navigate directly to the team page using the URL to see your changes.
1. Once ready, [stage and commit your changes](https://docs.gitlab.com/ee/topics/git/commit.html), with a comment *Add details for FirstName LastName to team page*.
1. [Push your branch](https://docs.gitlab.com/ee/topics/git/commit.html#send-changes-to-gitlab).
1. [Create a Merge Request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html) in [GitLab.com](https://gitlab.com/gitlab-com/www-gitlab-com) with the branch that you created and assign your manager as reviewer.

## Reviewing your changes

Once the MR is created, and you have a passing pipeline:

1. Look for the "View app" button in the pipeline widget on the "Overview" tab of the MR.
1. If the "View app" button does not take you to the correct page, manually visit the URL.
   - For example, use the domain of the review app `https://your-branch.about.gitlab-review.app/` and add `company/team/` to form `https://your-branch.about.gitlab-review.app/company/team/` to preview your team page changes.
1. If you make changes, ensure that the latest pipeline has passed before you look at the preview. Otherwise, the latest changes will not be present.

## Add your pet(s) to the Team Pets Page

Using what you learned in the [steps above](#add-yourself-to-the-team-page), consider adding your pet(s) to the [Team Pets page](https://about.gitlab.com/company/team-pets/).

The main differences are the names and locations of things.

1. The picture should be `petname.jpg` or `petname.png` with the same [picture requirements](#picture-requirements).
1. Upload the picture to `sites/uncategorized/source/images/team/pets`.
1. Your pet information should be added to the end of the `data/pets.yml` file.
1. Your commit message can be similar to `Adding my dog Gary to the Team Pets Page`.
1. Assign your manager as the reviewer.
   - If your manager has a warning yellow triangle symbol on their avatar after adding them, they can approve, but not merge. Post in the `#mr-buddies` Slack channel after your manager has approved with a request to get it merged.
