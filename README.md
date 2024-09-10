# ModResorts Demo Application

## Building
This version of ModResorts has dependencies on WAS APIs. You can install the dependencies needed in your local maven repo with the following command:

```
mvn install:install-file -Dfile=was-dependency/was_public.jar -DpomFile=was-dependency/was_public-9.0.0.pom
```

## Intent of the App
This app is designed to show a series of use cases for modernizing from tWas to Liberty, modernizing from one Java version to another and to show how the WCA4J product can be used to remediate issues using it's LLM.

The default state of the repo covers ALL the uses cases listed above. In many demo scenarios you may not what to show all the possible use cases. Since most of these issues are sequential and independent you can complete (using automated steps) any scenarios that you do not want to show. In the scenario where you do not want to show the LLM remediation use cases scripts are provided to remove the offending code. 

## How to use this App

1. Fork this repo
    - Do not clone it, or try to create a branch
1. Complete the steps to get to your desired starting point (see below)
1. OPTIONAL: Create your OCP cluster and configure it to point to your forked repo if showing the full deployment in RHOCP
1. If you plan to give this specific demo multiple times you should create a fork for each demo as pipelines will by default hook to the main branch
1. During your demo you will create branches, update a merge code etc into your fork

## Stages and Capabilities of the App
1. tWas to Liberty Use Case with recipe issues and LLM issues
    - If you don't want to show recipes you execute them now
    - If you don't want to deal with LLM remediation run the script to remove that code
    - NOTE: If you undertake either of these 2 steps you have to rescan for analysis
1. Java to Java modernization with recipe issues and LLM issues
    - You rescan for analysis providing the Java versions to go to and from
    - If you want to exclude any earlier Java version changes, run those recipes
    - If you don't want to deal with LLM remediation run the script to remove that code
    - NOTE: If you undertake either of these 2 steps you have to rescan for analysis

### Examples and FAQ
- I clone the repo and load the default migration bundle. Why don't I see any java modernization issues?
    - The default migration modernizes from tWas on Java 8 to Liberty on Java 8, so Java modernization issues will be excluded
    - If you want to see Java modernization issues as well at this stage you need to rescan with a new java target level set
- I just want to show the LLM remediation for Java modernization, what do I do?
    - Execute the steps to configure the repo to sue Liberty
    - Execute the recipes
    - Run the script to remove the tWas to Liberty LLM issues
    - Rescan for the source and target Java's you want to go to
    - Apply the recipes
    - Rescan: You will not only have the LLM remediation issue for Java
 - More....     