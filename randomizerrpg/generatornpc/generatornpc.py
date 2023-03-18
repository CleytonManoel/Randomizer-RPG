from . import npcname, npcage, npcjob


def generator_npc(agetype,job,gender,breed):

    npcb = breed

    npcg = gender

    npcn = npcname.random_names(breed,gender)

    npca = npcage.random_age(agetype)

    npcj = npcjob.random_job(job,gender)

    return npcb,npcn,npcg,npca,npcj

