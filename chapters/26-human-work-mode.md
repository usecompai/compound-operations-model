# People and AI agents

A person using an AI client and a background agent are different execution identities. A scheduled job must not inherit every permission of its creator.

For interactive work, authenticate the person, load project context and use capabilities assigned to their role. Complete authorised work rather than asking the person to bridge connected systems manually.

For background work, assign a dedicated identity, bounded scope, allowed tools, budget and stop condition. Consequential actions outside that contract require approval.

Test the same job under both identities. Private records stay private. A denied action stays denied through alternative tools. Record the initiating and acting identities with the result.
