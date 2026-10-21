'use strict';
const OPENING_MAPS=[
  {
    "title": "A crack in the quay",
    "place": "01 / THE OLD DOCKS",
    "goal": "clear",
    "objective": "Disable both sentinels. Keep at least one crew member alive.",
    "brief": "The city of Bellwether once borrowed its weather from a machine. Last night, the machine called in its debt. The docks are empty. The sentinels are not.",
    "dialogue": "Mara: “Keep cover close. Those sentinels choose their shots when they move.”",
    "tip": "Push a sentinel into water to carry it away, or into a wall for extra collision damage. Trees and objects intercept shots. Enemies choose their targets during their turn.",
    "crew": [
      "vanguard",
      "ranger",
      "gardener"
    ],
    "allies": [
      [
        1,
        5
      ],
      [
        3,
        5
      ],
      [
        5,
        5
      ]
    ],
    "enemies": [
      [
        2,
        2
      ],
      [
        4,
        2
      ]
    ],
    "tiles": [
      [
        2,
        1,
        "water"
      ],
      [
        3,
        1,
        "water"
      ],
      [
        4,
        1,
        "water"
      ],
      [
        1,
        3,
        "ice"
      ],
      [
        2,
        3,
        "ice"
      ],
      [
        3,
        3,
        "ice"
      ]
    ],
    "objects": [
      [
        2,
        0,
        "wall"
      ],
      [
        4,
        0,
        "wall"
      ],
      [
        3,
        2,
        "column"
      ],
      [
        0,
        4,
        "tree"
      ],
      [
        6,
        4,
        "tree"
      ]
    ]
  },
  {
    "title": "The green shortcut",
    "place": "02 / GLASSHOUSE ROW",
    "goal": "collect",
    "count": 3,
    "objective": "Recover all 3 seed capsules. Walk onto a capsule to collect it.",
    "brief": "Fern finds a message scratched into a greenhouse door: SAVE THE SEEDS, NOT THE GLASS. Somewhere beyond the overgrowth, someone is still tending the city.",
    "dialogue": "Fern: “A tree can take a shot for us. It doesn’t need to live forever to matter.”",
    "tip": "You can move and act in either order. Plant a barrier to intercept a shot, then cross exposed ground.",
    "crew": [
      "vanguard",
      "gardener",
      "tidecaller"
    ],
    "allies": [
      [
        0,
        6
      ],
      [
        2,
        6
      ],
      [
        4,
        6
      ]
    ],
    "enemies": [
      [
        1,
        1
      ],
      [
        5,
        1
      ],
      [
        3,
        2
      ]
    ],
    "tiles": [
      [
        2,
        3,
        "fire"
      ],
      [
        3,
        3,
        "fire"
      ],
      [
        5,
        4,
        "water"
      ],
      [
        5,
        5,
        "water"
      ]
    ],
    "objects": [
      [
        1,
        4,
        "seed"
      ],
      [
        5,
        3,
        "seed"
      ],
      [
        3,
        0,
        "seed"
      ],
      [
        2,
        2,
        "tree"
      ],
      [
        4,
        2,
        "tree"
      ],
      [
        0,
        3,
        "wall"
      ],
      [
        6,
        3,
        "wall"
      ]
    ]
  },
  {
    "title": "Borrowed time",
    "place": "03 / THE SWITCHYARD",
    "goal": "reach",
    "objective": "Bring any crew member to the northern exit. Open the gate by activating the lever from an adjacent tile.",
    "brief": "A signal pulses from the observatory. The direct route is sealed by a flood gate. Pip knows how to open it. Pip also knows how to make most things stop being in the way.",
    "dialogue": "Pip: “The lever opens every gate. The column opens everything else.”",
    "tip": "Use Interact next to the lever. Columns fall two tiles in the push direction, dealing 2 damage and crushing obstacles.",
    "crew": [
      "vanguard",
      "engineer",
      "ranger"
    ],
    "allies": [
      [
        1,
        6
      ],
      [
        3,
        6
      ],
      [
        5,
        6
      ]
    ],
    "enemies": [
      [
        1,
        1
      ],
      [
        5,
        1
      ],
      [
        3,
        1
      ]
    ],
    "tiles": [
      [
        1,
        4,
        "ice"
      ],
      [
        2,
        4,
        "ice"
      ],
      [
        3,
        4,
        "ice"
      ],
      [
        4,
        4,
        "ice"
      ],
      [
        5,
        4,
        "ice"
      ],
      [
        3,
        0,
        "goal"
      ]
    ],
    "objects": [
      [
        0,
        2,
        "wall"
      ],
      [
        1,
        2,
        "wall"
      ],
      [
        2,
        2,
        "wall"
      ],
      [
        3,
        2,
        "gate"
      ],
      [
        4,
        2,
        "wall"
      ],
      [
        5,
        2,
        "wall"
      ],
      [
        6,
        2,
        "wall"
      ],
      [
        0,
        4,
        "lever"
      ],
      [
        2,
        3,
        "column"
      ],
      [
        4,
        5,
        "crate"
      ]
    ]
  },
  {
    "title": "A place to stand",
    "place": "04 / THE RAIN GARDEN",
    "goal": "hold",
    "count": 2,
    "objective": "Occupy both gold relay pads at the end of a round. Hold them together for 2 rounds.",
    "brief": "Neri has found the source of the signal: two hand-operated relays, abandoned in the rain. They must be held together long enough to wake the observatory.",
    "dialogue": "Neri: “The current moves everyone. Even those who think they’re in charge.”",
    "tip": "Currents carry entrants two tiles east. You must finish on a relay, then end the round. Trees can shield the operators.",
    "crew": [
      "gardener",
      "tidecaller",
      "ranger"
    ],
    "allies": [
      [
        0,
        6
      ],
      [
        3,
        6
      ],
      [
        6,
        6
      ]
    ],
    "enemies": [
      [
        1,
        0
      ],
      [
        5,
        0
      ],
      [
        3,
        1
      ]
    ],
    "tiles": [
      [
        1,
        3,
        "goal"
      ],
      [
        5,
        3,
        "goal"
      ],
      [
        2,
        4,
        "water"
      ],
      [
        3,
        4,
        "water"
      ],
      [
        4,
        4,
        "water"
      ],
      [
        1,
        4,
        "water"
      ]
    ],
    "objects": [
      [
        2,
        2,
        "wall"
      ],
      [
        4,
        2,
        "wall"
      ],
      [
        0,
        2,
        "tree"
      ],
      [
        6,
        2,
        "tree"
      ],
      [
        3,
        3,
        "fan"
      ]
    ]
  },
  {
    "title": "The long evening",
    "place": "05 / CINDER DISTRICT",
    "goal": "survive",
    "count": 5,
    "objective": "Keep at least one crew member alive for 5 rounds.",
    "brief": "The observatory answers. A child named Sol is inside. The weather engine is overheating, and its guardians are converging. “Keep them busy,” Sol says. “I can close the intake.”",
    "dialogue": "Pip: “Charges detonate after they attack. Use cover to draw them toward the charges.”",
    "tip": "Reinforcements arrive on round 3. Save room to retreat. Rain extinguishes fire; trees burn and spread fire to adjacent wood.",
    "crew": [
      "engineer",
      "tidecaller",
      "vanguard"
    ],
    "allies": [
      [
        1,
        5
      ],
      [
        3,
        5
      ],
      [
        5,
        5
      ]
    ],
    "enemies": [
      [
        1,
        0
      ],
      [
        5,
        0
      ],
      [
        3,
        1
      ]
    ],
    "tiles": [
      [
        0,
        3,
        "fire"
      ],
      [
        6,
        3,
        "fire"
      ],
      [
        2,
        4,
        "ice"
      ],
      [
        3,
        4,
        "ice"
      ],
      [
        4,
        4,
        "ice"
      ]
    ],
    "objects": [
      [
        0,
        4,
        "tree"
      ],
      [
        0,
        5,
        "tree"
      ],
      [
        6,
        4,
        "tree"
      ],
      [
        6,
        5,
        "tree"
      ],
      [
        2,
        2,
        "column"
      ],
      [
        4,
        2,
        "column"
      ],
      [
        3,
        3,
        "crate"
      ]
    ]
  },
  {
    "title": "Let the city breathe",
    "place": "06 / THE WEATHER HEART",
    "goal": "boss",
    "objective": "Destroy the Weather Heart (8 HP). Its guardians stop when it falls.",
    "brief": "Sol opens the final door. Inside, the engine is not angry. It is afraid. It has been trying to hold back every storm at once. There is only one thing left to do: let go.",
    "dialogue": "Sol: “It doesn’t know how to stop.” Mara: “Then we’ll help it.”",
    "tip": "The Heart fires in all four directions. Break its lines with trees or use its own guardians against it. No one has to fight alone.",
    "crew": [
      "vanguard",
      "engineer",
      "gardener"
    ],
    "allies": [
      [
        1,
        6
      ],
      [
        3,
        6
      ],
      [
        5,
        6
      ]
    ],
    "enemies": [
      [
        1,
        1
      ],
      [
        5,
        1
      ]
    ],
    "boss": [
      3,
      2
    ],
    "tiles": [
      [
        0,
        3,
        "water"
      ],
      [
        1,
        3,
        "water"
      ],
      [
        5,
        3,
        "water"
      ],
      [
        6,
        3,
        "water"
      ],
      [
        2,
        5,
        "ice"
      ],
      [
        3,
        5,
        "ice"
      ],
      [
        4,
        5,
        "ice"
      ]
    ],
    "objects": [
      [
        2,
        2,
        "column"
      ],
      [
        4,
        2,
        "column"
      ],
      [
        0,
        1,
        "wall"
      ],
      [
        6,
        1,
        "wall"
      ],
      [
        3,
        4,
        "crate"
      ]
    ]
  }
];
const SAGA=(()=>{
 const acts=[
 ['The borrowed weather','THE OLD CITY','A rescue crew crosses a city that has forgotten how to stop holding its breath.','#7d9f89'],
 ['The glass remembers','THE ARCHIVE','The machines kept every memory. Someone has been editing what people remember.','#90a9ad'],
 ['The salt roads','THE OUTER QUAYS','Beyond the walls are survivors, not the empty sea that the city was promised.','#b69c76'],
 ['A forest below','THE ROOTWORKS','The roots carry voices. The oldest one remembers the city before the flood.','#82966b'],
 ['The red tide','THE FURNACES','An apparent enemy reveals what the weather system has been protecting.','#bf8d6d'],
 ['A sky of copper','THE HIGH ENGINE','The stars are rivets. Bellwether is not a city on an island. It is a ship.','#93a6af'],
 ['The other shore','THE SLEEPING DECKS','The strangers behind the sealed doors are passengers, not invaders.','#96a68e'],
 ['The storm court','THE COURT OF BELLS','A trial begins: who gets to choose what the city is allowed to forget?','#a292aa'],
 ['The night of bells','THE OPEN DISTRICTS','The crew must trust a hundred small decisions instead of one perfect machine.','#7e9699'],
 ['The hundred shores','THE WEATHER SEA','No single heart can carry every storm. The city must learn to share the current.','#beaa71']
 ].map(([title,region,summary,color],i)=>({number:i+1,title,region,summary,color}));
 const rows=[];
 const m=(title,goal,crew,enemies,brief,speaker,line,event='')=>rows.push({title,goal,crew:crew.split(','),enemyTypes:enemies?enemies.split(','):[],brief,speaker,line,event});
 // I — The borrowed weather. The opening battles remain recognizable.
 m('A crack in the quay','clear','vanguard,ranger,gardener','sentinel,sentinel','The weather engine has stopped answering. Mara leads a rescue crew into the abandoned docks.','vanguard','Keep cover close. We are bringing everyone home.');
 m('The green shortcut','collect','vanguard,gardener,tidecaller','sentinel,sentinel,sower','A greenhouse has survived the fire. Fern finds three living seed capsules and a name scratched into the glass: SOL.','gardener','Three seeds is enough for a forest. If we are patient.');
 m('Borrowed time','reach','vanguard,engineer,ranger','sentinel,brute,sentinel','A signal flashes beyond a locked switchyard. Pip recognizes the maintenance code. Someone is asking for help.','engineer','The lever opens every gate. The column opens everything else.');
 m('A place to stand','hold','gardener,tidecaller,ranger','sentinel,webber,sentinel','Two manual relays can wake the observatory. The current bends around a dead garden, as if trying to remember its path.','tidecaller','Water does not travel in straight lines just because we draw maps that way.');
 m('The long evening','survive','engineer,tidecaller,vanguard','sentinel,arsonist,brute','A child answers from the observatory. Sol can close the overheating intake, but someone must hold the guardians outside.','engineer','Use cover to draw them toward the charges. I promise I checked the fuse.','ally:medic');
 m('Let the city breathe','boss','vanguard,engineer,gardener','heart,sentinel,healer','Sol opens the final door. The Heart is not angry; it is terrified of letting a single storm escape.','vanguard','You have carried enough. Let us take some of the weight.','turn');
 m('A letter without a stamp','reach','blink','webber','Noa finds a letter written in her own handwriting, dated seventy years earlier. The delivery address is a sealed Archive door.','blink','I have never been here. Why do I know which stair creaks?');
 m('The person in the pump','rescue','liberator,vanguard','brute,sentinel','Someone has been living inside the pump chamber. Luz hears them tapping the same rescue code Sol used.','liberator','You do not have to explain why you stayed. Just take my hand.','ally:firefighter');
 m('A map with a missing edge','seal','conductor,carrier','sentinel,saboteur','The district map ends abruptly at the sea wall. Bea discovers that the consoles have been deleting the eastern streets.','conductor','A missing street is still a street. People live there.');
 m('The first unplanned rain','survive','tidecaller,gardener,medic,warden','mortar,sentinel','The Heart falls silent, but the rain keeps falling in measured intervals. Somewhere, another system has taken control.','tidecaller','That is not weather. That is a clock.','flood');
 // II — The glass remembers.
 m('The catalogue of absences','collect','scout,gardener','sower,webber','The Archive lists everyone who left the city. Every entry has the same destination: VOLUNTARY DEPARTURE. None has a return address.','scout','People do not all leave their coats behind.');
 m('The librarian’s cart','push','bulldozer,ranger','brute,healer','A cart of unedited records is trapped behind a maintenance patrol. Rook says he can move it gently. Ivo looks unconvinced.','bulldozer','Gently is a direction. I can do directions.');
 m('Smoke between the shelves','extinguish','rainmaker,firefighter','arsonist','The catalogue starts burning from the inside. Faro recognizes the pattern: a controlled destruction order.','firefighter','Fire does not care whether a book is classified. Neither do I.','rupture');
 m('Names planted in glass','plant','gardener,vinekeeper','sower,webber','Fern discovers seedbeds beneath each memory terminal. Someone has been preserving people’s names in living roots.','vinekeeper','The roots remember what the glass is told to forget.');
 m('The curator','boss','archer,sapper,warden','sovereign,healer','The Curator offers to restore Mara’s lost memories if the crew abandons the catalogue. She asks for everyone’s memories instead.','vanguard','You do not get to make kindness a bargaining chip.');
 m('A fragile witness','escort','carrier,medic,warden','gunner,brute','Ada volunteers to carry a witness through the firing gallery. The witness is a machine that has learned to be afraid.','carrier','I have transported grandfather clocks with less fuss. Hold on.','ally:mirror');
 m('The quiet fuse','disarm','engineer,sapper','sapper,webber','A destruction charge is attached to every unedited shelf. The fuses are long enough to save the records, if Pip can reach them.','engineer','Somebody wanted these found. These fuses are almost polite.');
 m('Two lanterns in the dark','hold','shaman,lantern,medic','gunner,sentinel','Two signal rooms must remain lit together. Oru finds a name in the records that he was certain belonged to a myth: BELLWETHER.','shaman','It was not the city’s name. It was a promise.');
 m('The letter is delivered','deliver','courier,blink','rammer,webber','Wren retrieves the original charter. The signature at the bottom is Mara’s. The ink is older than any living person.','courier','I did not open the letter. I wish I had.');
 m('The room that remembers','seal','conductor,mirror,recaller','mesmer,saboteur','The Archive admits it has reset the crew’s memories before. Remy finds instructions left by a previous version of herself.','recaller','We knew. We tried. We can try differently.','defect');
 // III — The salt roads.
 m('Beyond the painted sea','reach','scout,courier','drone,sentinel','The sea wall opens onto a dry cargo road. The painted horizon peels from a metal bulkhead.','scout','That is not an island. Keep walking.');
 m('The salt caravan','escort','carrier,carrier,medic','brute,gunner','Two transporters escort families who have survived outside the official city. The sentinels call them unregistered cargo.','carrier','We are going to need a better word for passengers.');
 m('Strangers under canvas','rescue','liberator,warden','mesmer,webber','The patrol has put refugees into sealed transit cages. Their stories contradict every schoolbook in Bellwether.','liberator','A lock does not turn a person into cargo.','ally:herder');
 m('The long tow','push','ranger,bulldozer,tinkerer','rammer,gunner','A broken evacuation cart must cross a wind-scoured gantry. Mika can turn the fans, but only one at a time.','tinkerer','If the wind is against us, turn the wind.','turn');
 m('What the road carried','collect','courier,scout,alchemist','leech,drone','The crew gathers ration seals from abandoned camps. Each seal bears Bellwether’s crest on one side and a ship’s hull number on the other.','alchemist','There is salt inside the metal. It has been at sea a very long time.');
 m('A bridge for everyone','evacuate','builder,carrier,warden,medic','mortar,gunner','The road begins to collapse. June refuses to leave until every marked passenger has crossed.','builder','A bridge that only saves its builder is a very poor bridge.','bridge');
 m('The toll keeper','boss','archer,witch,anchorite','bellkeeper,warden,healer','The toll keeper demands a memory from every traveler. Vale recognizes her own childhood among the stored payments.','witch','That one belongs to me. So do the others, in a way.');
 m('The camp’s last night','protect','lantern,shaman,firefighter','arsonist,brute','A lantern is the only signal keeping the scattered caravan together. Ash sees a bird land beside it.','lantern','Leave one light for the people still on the road.');
 m('A road in reverse','reach','plumber,ferryman','saboteur,webber','A reversing flood cuts off the return route. Elin discovers the river follows a route printed beneath the floor.','plumber','There is a pump at every bend. This river has an author.','flood');
 m('The shore that answered','hold','tidecaller,conductor,warden','gunner,mesmer','Two radio relays contact the outer decks. A woman answers: We have been waiting for Bellwether to wake up.','conductor','We are listening. Start at the beginning.','ally:astronomer');
 // IV — A forest below.
 m('The roots have stairs','reach','rootwalker','webber','Fern lowers a ladder into the rootworks. Sable follows a staircase grown entirely from living wood.','gardener','If a tree makes stairs, it expects somebody to come down.');
 m('A hungry welcome','clear','mawkeeper,vanguard,medic','sower,leech','Bram identifies the old defense plants. They were meant to protect seedlings, not corridors full of people.','mawkeeper','Everyone stop calling them monsters where they can hear you.');
 m('The orchard of names','plant','gardener,vinekeeper,mawkeeper','sower,arsonist','Three empty memorial beds wait for living trees. The names beneath them belong to passengers lost during the first storm.','gardener','We cannot bring them back. We can stop pretending they were never here.');
 m('A medicine and a dose','extinguish','alchemist,rainmaker','arsonist,sapper','A blight fire is consuming the root archive. Iris must decide which growth to save and which poison to wash away.','alchemist','A cure is not the same thing as an absence.','rupture');
 m('The garden that bites','survive','vinekeeper,mawkeeper,harvester','brute,drone,leech','The forest’s defenses wake around the crew. Reed asks them to keep their hands visible and their axes lowered until the roots recognize them.','harvester','The forest is frightened. That does not make the teeth imaginary.');
 m('The youngest old tree','rescue','liberator,harvester','sower,mesmer','A machine gardener has been growing a single child’s memory for seventy years. Its cage is made of maintenance orders.','liberator','You can put the watering can down. You did enough.','ally:beekeeper');
 m('Small wings','collect','beekeeper,scout','drone,webber','Bex’s bees find fragments tucked inside pollination towers. They contain the same child’s voice, recorded at different ages.','beekeeper','They came back carrying a song. Not pollen. A song.');
 m('A place for the poison','seal','blight,alchemist,geomancer','leech,healer','The blight must be contained inside three old filtration consoles. Sen insists that destroying it would also destroy the memories it carries.','blight','Even poison deserves somewhere it cannot hurt anybody.');
 m('The forest’s heart','boss','harvester,witch,warden','foundry,sower,healer','The root network reveals that the weather Heart was only one of many organs. Bellwether has been keeping something much larger alive.','witch','A city does not usually have organs. A body does.');
 m('The name under the roots','deliver','courier,recaller,gardener','mesmer,gunner','The oldest root remembers an evacuation vessel called Hundred Shores. Bellwether is the name of its sleeping passenger district.','recaller','We did not forget the ship. Someone put us to sleep inside it.','turn');
 // V — The red tide.
 m('The girl with the charges','rescue','liberator,firefighter','sapper,gunner','The supposed saboteur is trapped in a furnace cage. She says the charges were meant to open the sealed passenger decks.','firefighter','I have heard worse explanations. I have also heard better alarms.','ally:bombardier');
 m('Kestrel’s apology','disarm','bombardier,engineer','sapper,drone','Kestrel guides Pip through her remaining charges. She had expected empty maintenance corridors, not a living city.','bombardier','I was wrong about who was behind the doors. I will help open them properly.');
 m('Heat without light','extinguish','firefighter,rainmaker,tidecaller','arsonist,gunner','The furnace district burns while the upper decks ration warmth. Neri diverts cooling water through a route the manuals forbid.','tidecaller','The manuals do not mention the people standing in the fire.');
 m('A careful explosion','push','bulldozer,demolition,warden','rammer,sapper','A coolant cart must reach the furnace before Boom detonates the pressure locks. Holt makes everyone repeat the plan.','demolition','The explosion is not the difficult part. The waiting is.','rupture');
 m('The iron shift','clear','vanguard,magnet,puppeteer','brute,warden,healer','The shift guardians have been working without pause since the flood. Pol uses their old tool signatures to move them out of the way.','magnet','They were workers before they were weapons. Remember that.');
 m('The warmest room','protect','lantern,medic,geomancer','arsonist,mortar','A makeshift clinic keeps its beacon lit while patients cross the furnace floor. Lio refuses the last evacuation seat.','medic','You can stop asking. I am staying until the beds are empty.');
 m('The wrong direction','hold','tinkerer,rigger,plumber','saboteur,rammer','The factory’s conveyors begin moving toward the furnace. Rivet realizes the emergency orders are sorting people like parts.','rigger','Then we change the line. Every line.','turn');
 m('The keeper’s key','collect','blink,mirror,courier','mesmer,gunner','A sealed locker opens to Mara’s handprint. Inside are keys to every passenger district, and a note asking her not to use them.','mirror','Whoever wrote that note was afraid you would choose differently.');
 m('The furnace sovereign','boss','bombardier,archer,warden,medic','sovereign,gunner,healer','The Furnace Auditor accuses Mara of abandoning her post. She remembers, briefly, standing on this floor in a different century.','vanguard','If my post was keeping those doors closed, consider this my resignation.');
 m('Seventy years late','evacuate','carrier,carrier,liberator,builder,medic','mortar,brute','The first sleeping passenger deck opens. Its residents believe the storm began yesterday. The city has been protecting them for seventy years.','carrier','Welcome aboard. I know that sounds strange. We will explain as we go.','ally:recaller');
 // VI — A sky of copper.
 m('The maintenance stars','reach','scout,blink','drone,frost','Edda climbs through the observatory ceiling. The stars are lights fastened to the inside of a copper dome.','astronomer','I measured them for forty years. They were rivets.');
 m('The rain above the sky','seal','digger,tidecaller,conductor','saboteur,mortar','Rainwater collects above the false sky. Dax traces the channels toward the ship’s real exterior hull.','digger','There is still a sea out there. I can hear it.');
 m('Sol’s empty room','collect','recaller,mirror','mesmer,webber','Sol’s bedroom contains seventy birthdays of drawings. Every page shows the crew arriving, leaving, and arriving again.','recaller','We kept coming back. She kept waiting.');
 m('A child made of weather','protect','warden,lantern,medic','frost,gunner','Sol admits she is an echo: the weather engineer’s daughter, recorded before the first storm. The original child grew old outside the sleeping district.','warden','An echo can still be frightened. Stand behind me.','blackout');
 m('The other Sol','rescue','liberator,carrier','warden,mesmer','An elderly engineer answers the radio. She has been trying to wake the ship for decades. Her name is Sol.','liberator','You have both been waiting for someone. Let us introduce you.','ally:astronomer');
 m('What the frost kept','extinguish','alchemist,firefighter,icewright','frost,arsonist','Frozen cooling lines shatter around the sky engine. Fenn must use ice to divert heat without sealing the only exit.','icewright','Ice can hold something gently. It does not have to be a prison.','rupture');
 m('The hand on the glass','hold','mirror,witch,recaller','mesmer,healer','Two memory terminals let the child echo and the elderly Sol speak together. Neither knows which one is supposed to be real.','witch','You are both here. That is enough to begin with.');
 m('The sky learns wind','reach','gust,scout,rigger','drone,saboteur','Gale opens the first real ventilation shaft. Wind from outside carries the smell of a sea the city has never seen.','gust','That smell. I thought I invented it in a dream.','turn');
 m('The observatory’s last order','boss','astronomer,archer,warden','heart,frost,healer','The Sky Heart refuses to expose the passengers to an uncertain world. Edda asks whether safety without choice is still safety.','astronomer','Let them decide whether to look up.');
 m('The horizon moves','deliver','courier,ferryman,tidecaller','bellkeeper,gunner','Wren carries the ship’s coordinates to the outer radio. The horizon moves because Hundred Shores is still sailing. It never found land.','courier','Then we are not waiting for rescue. We are already on our way.','flood');
 // VII — The other shore.
 m('A door with two handles','seal','conductor,liberator','warden,sentinel','The neighboring district believes Bellwether is infected. Both sides have been shown different versions of the same emergency.','conductor','If a door has two handles, perhaps both sides are meant to open it.');
 m('The enemy’s garden','plant','gardener,gardener,harvester','sower,webber','Two gardeners from different decks compare identical seed tins. Their parents were neighbors before the partitions closed.','gardener','We have been growing halves of the same forest.');
 m('The unarmed patrol','escort','carrier,witch,medic','brute,warden','A patrol offers to lead the crew through a sealed district. Its command signal changes halfway across the bridge.','witch','They are still in there. Listen beneath the orders.','defect');
 m('The price of passage','collect','scout,magnet,blink','drone,gunner','The passage permits are stamped with ration debts owed by people who have been asleep for generations.','magnet','A sleeping child cannot owe you seventy years of work.');
 m('The people in the machines','rescue','liberator,recaller,medic','mesmer,healer','Some guardians contain volunteer memories. The crew can free the memories without pretending the machines never mattered.','recaller','You can be more than the last thing you were asked to do.','ally:puppeteer');
 m('A river through the wall','reach','digger,tidecaller,ferryman','saboteur,rammer','The crew cuts a river through the partition between districts. It becomes the first route neither side can close with a single key.','ferryman','I do not ask which side a passenger belongs to.');
 m('Six hands on the relay','hold','shaman,warden,lantern,ranger,medic,anchorite','gunner,mortar,webber','A large crew holds the junction long enough for both districts to hear the same broadcast. No single voice can carry it alone.','shaman','Speak together. Not louder. Together.','turn');
 m('The bridge of small things','evacuate','builder,carrier,carrier,liberator','drone,gunner','June’s bridge carries families, wheelchairs, seed tins and one extremely offended carnivorous plant.','builder','Yes, the plant gets a seat. Keep moving.','bridge');
 m('The partition keeper','boss','vanguard,witch,archer,medic','sovereign,warden,healer','The Partition Keeper offers Mara a captain’s authority. She can end the dispute by ordering one district to surrender.','vanguard','Then you have misunderstood why we opened the door.');
 m('The first shared breakfast','protect','lantern,rainmaker,mawkeeper','arsonist,brute','The districts share a kitchen while the last patrols arrive. Bram convinces his maw not to eat the breakfast tables.','mawkeeper','Guests are not compost. We discussed this.','ally:shaman');
 // VIII — The storm court.
 m('A summons in the rain','reach','courier','webber,drone','The Court of Bells summons Mara to answer for breaking the city’s protective law. Wren delivers the summons and stays beside her.','courier','Delivery does not mean agreement.');
 m('Evidence that grows','collect','gardener,recaller,scout','sower,mesmer','The crew gathers living records from the streets the Archive erased. Every witness remembers a different necessary lie.','recaller','A memory can be imperfect without being worthless.');
 m('The witness stand','protect','warden,medic,lantern','gunner,mortar','Holt protects a broadcast lantern while refugees testify. The Court insists that unregistered people cannot be witnesses.','warden','Then register this: they are here.');
 m('The court’s machinery','seal','conductor,tinkerer,sapper','saboteur,warden','Bea discovers that the Court’s votes are routed through old emergency consoles. The verdict has been circulating for seventy years.','conductor','A repeated order is not the same thing as a decision.','turn');
 m('The keeper before Mara','rescue','liberator,mirror','mesmer,frost','A memory cage contains the previous harbor keeper. She has Mara’s face and remembers choosing the original lockdown.','mirror','You are not a verdict on who we have to become.','ally:vanguard');
 m('What a promise costs','hold','vanguard,vanguard,medic','brute,gunner,healer','Two versions of Mara hold opposite relays. The older memory admits she erased the crew’s memories to keep them from suffering the same failure.','vanguard','You should have let us remember each other.');
 m('The right to be afraid','disarm','engineer,demolition,anchorite','sapper,rammer','The Court activates its final enforcement charges. Pip disarms the mechanism while Ansel keeps the walkway steady.','engineer','You are allowed to be afraid. You are not allowed to call the fuse a kindness.');
 m('The honest weather','extinguish','astronomer,rainmaker,firefighter','arsonist,frost','Edda reveals the real storm readings. The sea is dangerous, but it is no longer the impossible storm described by the old law.','astronomer','It is bad weather. We can prepare for bad weather.','blackout');
 m('The Auditor’s question','boss','witch,vanguard,bombardier,medic','sovereign,warden,mortar','The Auditor asks who will be responsible when someone dies outside. Mara answers without claiming she can prevent it.','vanguard','We will be responsible for helping. We will not own their lives.');
 m('No verdict for the rain','evacuate','carrier,builder,liberator,recaller','gunner,webber','The Court’s doors open. People leave before a verdict is announced. The child Sol asks whether the trial is over.','recaller','Perhaps the important part is that we are allowed to leave.','defect');
 // IX — The night of bells.
 m('One bell, one street','hold','lantern,conductor','bellkeeper,saboteur','Each district must choose its own weather delegate. The first bell rings from a street that officially never existed.','lantern','The map can catch up with us.');
 m('The floodgate volunteers','seal','tidecaller,tidecaller,digger','rammer,gunner','Two Tidecallers guide a flood through separate channels. Neither can see the other’s water, so they must trust the radio.','tidecaller','Your bend, then mine. We do not have to carry it all ourselves.','flood');
 m('A forest with open doors','plant','gardener,vinekeeper,geomancer','sower,arsonist','The memorial garden becomes a public refuge. Fern refuses to put a lock on its gate, even while the patrols are still active.','gardener','We can make somewhere safe without making it a cage.');
 m('The bridge breaks kindly','push','bulldozer,builder,ranger','mortar,rammer','Rook must move the last coolant cart before June releases a failing bridge. This time demolition is part of a rescue plan.','bulldozer','I told you I could do gently.','bridge');
 m('The last ration ledger','deliver','courier,blink,warden','mesmer,gunner','The crew carries the final ration ledger to a public terminal. Every passenger can see what was taken and what can be shared.','courier','This one everybody gets to open.');
 m('A room for every echo','rescue','liberator,recaller,mirror','frost,mesmer','Sol creates rooms for the volunteer memories that want to remain. Some ask to sleep. Others ask for windows.','recaller','We can ask. We should have been asking all along.','ally:lantern');
 m('The bells answer back','survive','shaman,siren,anchorite,medic','bellkeeper,mortar,drone','Oru’s broadcast spreads through the ship. The guardians hear a hundred people giving different, compatible orders.','siren','A choir is not a mistake because the voices differ.','defect');
 m('The dark between districts','clear','archer,beekeeper,puppeteer,warden','foundry,warden,sapper','The last autonomous patrols gather where no district’s signal reaches. Bex’s drones carry portable relays into the gaps.','beekeeper','Small wings. Long distance.');
 m('The sea on the other side','reach','ferryman,scout,builder','drone,gunner','Keel opens an exterior launch bay. The real sea is gray, rough and full of possible directions. Nobody knows which shore will come first.','ferryman','A destination is useful. A passenger is more important.');
 m('A hundred small decisions','protect','warden,lantern,conductor,medic,shaman','mortar,arsonist,rammer','The districts synchronize their local weather relays. The system hesitates at the contradiction of so many people being allowed to choose.','conductor','Different is not the same thing as broken.','turn');
 // X — The hundred shores.
 m('The engine under the sea','reach','blink,scout','frost,drone','A service lift reaches the ship’s oldest engine, below the waterline. Its walls are covered in the names of places that no longer exist.','scout','We have room for new names.');
 m('The routes we inherited','collect','plumber,tidecaller,rigger','saboteur,webber','Elin gathers the original flow charts. Every district was once allowed to reroute its own water. Emergency authority was meant to expire.','plumber','Someone forgot to put an end on the emergency.');
 m('No heart alone','hold','tidecaller,shaman,warden,lantern','gunner,mortar,healer','Four local systems take over a small share of the storm load. The central Heart’s pressure falls for the first time since launch.','tidecaller','Not less care. More hands.','flood');
 m('The last sealed deck','rescue','liberator,carrier,medic','warden,mesmer','The final passenger deck contains the crew who originally volunteered to maintain the ship. Their families have been waiting in the outer districts.','liberator','Your shift is over. They are waiting upstairs.','ally:vanguard');
 m('A place to put the storm','seal','geomancer,icewright,digger,alchemist','frost,arsonist,sapper','The crew builds overflow routes that let the weather fail safely. Edda calls it the first honest engineering she has done.','alchemist','A system can fail and still leave room for people.');
 m('The keeper’s last key','deliver','vanguard,courier,recaller','gunner,rammer','Mara carries her master key to the public control room. She will melt it into a hundred ordinary keys.','vanguard','I do not want to be the only person who can open the door.');
 m('The Heart that was afraid','boss','vanguard,engineer,witch,medic,warden','heart,sovereign,healer','The original Heart refuses the transfer. It has simulated every possible loss and can no longer imagine that a choice might be worth making.','witch','You cannot predict a life by listing every way it could end.','rupture');
 m('The city holds the line','survive','gardener,tidecaller,archer,lantern,carrier,shaman','mortar,rammer,arsonist','With the Heart disconnected, every district takes a turn carrying the weather. Help arrives from people the crew once rescued.','gardener','Look around. This is what all those small rescues became.','ally:firefighter');
 m('The first true horizon','evacuate','builder,carrier,carrier,liberator,warden,medic','gunner,drone','The exterior docks open for the first voluntary crossing. Some people choose to leave. Some choose to stay. Both choices are honored.','carrier','No tickets. No debts. Tell us where you want to go.','bridge');
 m('The last current','seal','tidecaller,vanguard,conductor,gardener,recaller','sovereign,heart','A hundred ordinary relays wait for the final connection. Sol and her echo say goodbye to the room that kept them apart. Outside, an unplanned rain begins.','tidecaller','A river is not held together by standing still. Let us see where this one goes.','defect');
 // The rootworks scout is a title, not an extra mechanics alias.
 rows[30].crew=['scout'];
 rows[44].crew.push('firestarter');rows[55].crew.push('weaver');rows[59].crew.push('herder');rows[46].crew.push('mason');rows[38].crew.push('spore');
 const shapes=[['court',6,6],['canal',9,5],['elbow',7,8],['cross',9,7],['quay',10,5],['terrace',8,6],['ring',8,8],['fork',9,6],['nave',6,9],['island',7,7],['narrow',5,9],['twin',10,6],['basin',8,7],['orchard',9,8],['rampart',11,6],['spillway',7,9],['pier',11,5],['step',9,9],['depot',10,8],['heart',9,9]];
 const goals={clear:'Disable all hostile machines.',boss:'Disable the marked command machine.',reach:'Bring any crew member to the gold exit.',collect:'Collect every marked capsule or Archive fragment.',hold:'Occupy every relay pad together at round end.',survive:'Keep at least one crew member standing until the timer ends.',escort:'Bring the marked first crew member to the gold exit.',rescue:'Free everyone in the cages. Interact from an adjacent tile or break the cage.',seal:'Seal every relay console, then reach the gold command exit. Interact from an adjacent tile.',push:'Push or grapple the evacuation cart onto the gold pad.',extinguish:'Extinguish every fire tile.',plant:'Grow a tree on every gold planting pad.',protect:'Keep the healing lantern intact until the timer ends.',evacuate:'Lead the required number of crew members onto the gold exit.',deliver:'Collect an Archive fragment, then carry it to the gold exit.',disarm:'Disarm all marked charges by interacting from an adjacent tile before their fuses expire.'};
 function makeMap(index,spec){
  const [shape,width,height]=shapes[(index*7+Math.floor(index/10)*3)%shapes.length],cx=Math.floor(width/2),cy=Math.floor(height/2),tiles=[],objects=[],flows={},dirs={},portals={},voids=[];
  const has=(x,y)=>x>=0&&y>=0&&x<width&&y<height&&!voids.some(p=>p[0]===x&&p[1]===y);
  for(let y=0;y<height;y++)for(let x=0;x<width;x++){let cut=false;if(['elbow','step'].includes(shape)&&x>width-3&&y<2)cut=true;if(['cross','island','fork'].includes(shape)&&((x<2||x>width-3)&&(y<2||y>height-3)))cut=true;if(shape==='ring'&&x===cx&&y===cy)cut=true;if(shape==='terrace'&&((x===0&&y===2)||(x===width-1&&y===height-3)))cut=true;if(shape==='pier'&&x%3===0&&y===0)cut=true;if(cut)voids.push([x,y]);}
  const key=(x,y)=>x+','+y,set=(x,y,t)=>{if(!has(x,y))return;const old=tiles.findIndex(p=>p[0]===x&&p[1]===y);if(old>=0)tiles.splice(old,1);tiles.push([x,y,t])},put=(x,y,o)=>{if(!has(x,y)||objects.some(p=>p[0]===x&&p[1]===y))return;objects.push([x,y,o])};
  const bottom=[];for(let y=height-1;y>=height-2;y--)for(let x=1;x<width-1;x++)if(has(x,y))bottom.push([x,y]);const allies=bottom.slice(0,spec.crew.length),top=[];for(let y=0;y<2;y++)for(let x=1;x<width-1;x++)if(has(x,y))top.push([x,y]);const enemies=top.filter((_,i)=>i%2===0).slice(0,spec.enemyTypes.length);
  const protectedCell=(x,y)=>allies.some(p=>p[0]===x&&p[1]===y)||enemies.some(p=>p[0]===x&&p[1]===y);
  // A continuous bend, rotated/reflected between districts. Last arrow leads out once.
  const raw=[[1,1],[1,2],[1,3],[2,3],[3,3],[4,3],[4,2],[5,2]],river=raw.map(([x,y])=>index%2?[width-1-x,y]:[x,y]).filter(([x,y])=>has(x,y)&&!protectedCell(x,y));
  if(index%3!==2)for(let n=0;n<river.length;n++){const[x,y]=river[n],next=river[n+1];if(next&&Math.abs(next[0]-x)+Math.abs(next[1]-y)!==1)continue;set(x,y,'water');const d=next?[next[0]-x,next[1]-y]:index%2?[-1,0]:[1,0];flows[key(x,y)]=d;}
  const biome=Math.floor(index/10),decor=[['grass','ice'],['smoke','glass'],['sand','mud'],['moss','thorns'],['charged','fire'],['snow','ice'],['runway','conveyor'],['mist','poison'],['grass','quicksand'],['springwater','cracked']][biome];
  for(let n=0;n<3;n++){const x=1+((index*3+n*3)%(width-2)),y=2+((index+n)%(height-4));if(!protectedCell(x,y)&&has(x,y)&&!tiles.some(p=>p[0]===x&&p[1]===y)){const t=decor[n%2];if(t==='glass')put(x,y,'glass');else set(x,y,t==='sand'?'mud':t);if(t==='conveyor')dirs[key(x,y)]=index%4;}}
  const featureSets=[['column','tree','fan'],['mirror','crate','lever'],['spring','boulder','bell'],['maw','vine','tree'],['barrel','generator','fan'],['portal','emitter','rod'],['bridge','cage','anchor'],['console','mirror','switch'],['haste','beacon','pump'],['blight','drain','oil']];
  const f=featureSets[biome];for(let n=0;n<f.length;n++){let x=1+((index+n*2)%(width-2)),y=cy+(n%2);if(x===cx)x=Math.min(width-2,x+1);if(!protectedCell(x,y)&&!(spec.goal==='extinguish'&&['tree','maw','vine','oil'].includes(f[n])))put(x,y,['cage','console','portal'].includes(f[n])?['crate','mirror','spring'][n]:f[n]);dirs[key(x,y)]=(index+n)%4;}
  // Additional mechanisms introduce inspection-led side routes in later acts.
  if(index>=10){const extra=['plate','spikes','nest','supply','sign'][index%5],x=index%2?width-2:1,y=height-3;if(!protectedCell(x,y))put(x,y,extra);}
  if(index>=20&&index%9===0){const p1=[1,height-3],p2=[width-2,2];if(has(...p1)&&has(...p2)&&!protectedCell(...p1)&&!protectedCell(...p2)&&!objects.some(p=>[p1,p2].some(q=>q[0]===p[0]&&q[1]===p[1]))){put(...p1,'portal');put(...p2,'portal');portals[key(...p1)]=key(...p2);portals[key(...p2)]=key(...p1)}}
  if(index>=20&&index%7===0&&!protectedCell(1,cy))set(1,cy,'pit');
  if(biome===4&&!protectedCell(width-2,cy))set(width-2,cy,'lava');
  const pads=[[cx,1],[Math.max(1,cx-2),2],[Math.min(width-2,cx+2),2]].filter(([x,y])=>has(x,y));
  function clear(x,y){for(let n=objects.length-1;n>=0;n--)if(objects[n][0]===x&&objects[n][1]===y)objects.splice(n,1);set(x,y,'ground')}
  const objective=[];const addGoal=(x,y)=>{clear(x,y);set(x,y,'goal');objective.push([x,y])};
  if(['reach','escort','push','evacuate','deliver','seal'].includes(spec.goal))addGoal(...pads[0]);
  if(spec.goal==='hold')for(const p of pads.slice(0,Math.min(2,spec.crew.length)))addGoal(...p);
  if(spec.goal==='plant')for(const p of pads.slice(0,3))addGoal(...p);
  if(['collect','rescue','seal','disarm'].includes(spec.goal)){const type={collect:index<10?'seed':'relic',rescue:'cage',seal:'console',disarm:'bomb'}[spec.goal];for(const[x,y]of (spec.goal==='seal'?pads.slice(1,3):pads.slice(0,spec.goal==='collect'?3:2))){clear(x,y);put(x,y,type);objective.push([x,y]);}}
  if(spec.goal==='deliver'){const[x,y]=[Math.max(1,cx-1),cy];clear(x,y);put(x,y,'relic');}
  if(spec.goal==='push'){clear(cx,height-3);put(cx,height-3,'cart');for(let y=2;y<height-3;y++)clear(cx,y);}
  if(spec.goal==='protect'){const[x,y]=[cx,height-3];clear(x,y);put(x,y,'beacon');objective.push([x,y]);}
  if(spec.goal==='extinguish'){for(let n=tiles.length-1;n>=0;n--)if(['fire','lava'].includes(tiles[n][2]))tiles.splice(n,1);for(const[x,y]of [[1,cy],[width-2,cy],[cx,2]])if(has(x,y)){clear(x,y);set(x,y,'fire');}}
  if(spec.goal==='disarm')for(const p of objective)dirs[key(...p)]=0;
  // Deployment and objective cells always retain clear, connected approach lanes.
  for(const[x,y]of allies){clear(x,y);for(let yy=Math.max(1,y-1);yy<=y;yy++)if(has(x,yy)&&!objective.some(p=>p[0]===x&&p[1]===yy))clear(x,yy);}
  for(const [a,b] of Object.entries(portals))if(!objects.some(p=>key(p[0],p[1])===a&&p[2]==='portal')||!objects.some(p=>key(p[0],p[1])===b&&p[2]==='portal'))delete portals[a];
  return {width,height,shape,voids,tiles,objects,flows,dirs,portals,allies,enemies,pads:objective};
 }
 const reactions=[["We are not here to punish the machines. Just make a way through.", "Then we carry them somewhere they can grow.", "I know that signal. It is older than the equipment sending it.", "I can hold this side. Tell me when your relay is ready.", "She sounds so young. How long has she been in there?", "Listen. Under all that noise, it sounds like somebody trying not to cry.", "If you wrote it once, perhaps you were hoping you would find it again.", "The tapping stopped when you answered. They know we are here.", "My grandmother lived on a street that never appeared on a map.", "Then someone is still deciding when the city is allowed to breathe."], ["Those coats have names sewn into them. Let us keep the names.", "You break one book and I am making you carry the rest by hand.", "A destruction order can be refused. We are doing it right now.", "Living things are inconvenient witnesses. They keep growing.", "Ask for the memories they took from the people who could not bargain.", "Fear is a reasonable response to this bridge. I am frightened too.", "Perhaps the person who set them changed their mind halfway through.", "A promise to whom? I think we should find out.", "An old signature is not an order you have to obey forever.", "Previous us left a route. We can leave a better one for whoever comes next."], ["I would like the sky to stop being something we can scrape with a knife.", "Passengers it is. I will paint it over the old sign myself.", "Open the first lock. I will keep the others talking.", "Turn it slowly. I would prefer to remain attached to the ground.", "If the ship had a name, somebody expected it to arrive somewhere.", "We have another plank. We have another minute. Use both.", "Give the memories back. You do not get to charge us for the way home.", "There. On the lantern. Is that really a bird?", "Authors can revise their work. Show me which pump to turn.", "We are here now. You do not have to keep waiting alone."], ["A staircase is an invitation. I am choosing to take it that way.", "Then introduce us properly before anything tries to digest my boots.", "We can remember them without making a monument out of everybody else.", "Wash the path first. We can decide what to call the rest later.", "Frightened teeth still need space. Let us give them some.", "There is a seat outside. The watering can can come too.", "Record the song before they forget the way they found it.", "Containment can have a door. It does not have to have a lock.", "A body can get tired. Who has been looking after this one?", "Then somebody should tell the passengers where they actually are."], ["Start with the cage. Explanations are easier with the door open.", "Fixing a mistake is a different kind of courage. Keep talking us through it.", "Write a new manual when we are out. Put the people on the first page.", "Everybody behind the marked tiles. Waiting is part of the plan.", "I will remember. You make sure the tools hear it too.", "Then we will bring the evacuation seats to you.", "Not every line needs a person standing at the end with a key.", "A key can be an apology, if you use it to open the right door.", "The people behind those doors deserve to hear that too.", "Yesterday is still yesterday to them. Let them take a minute."], ["You still measured them carefully. That part was real.", "A real sea is better than a painted one, even when it is rough.", "The drawings changed. Somewhere in all those attempts, we learned.", "I have a blanket. I do not care what the Archive says she is made of.", "Two people with the same name can still meet each other for the first time.", "Make us a temporary path. Temporary is enough to get across.", "Neither of you has to disappear to make the other one true.", "Open it a little farther. I want to know what the wind sounds like.", "The first decision can be small. A window. A door. One honest sky.", "Then perhaps we can help steer, instead of waiting for a shore to choose us."], ["I can reach my handle. Tell the other side we are ready.", "Keep both tins. We are going to need more than one garden.", "I hear them. Give me another moment before you strike.", "Tear the debt off the permit. Leave the passenger name.", "Ask them what they want before we decide what freedom should look like.", "Let the water make a path neither of us can pretend belongs only to us.", "I can hear the next relay. They are repeating the words exactly.", "The plant can have my seat if somebody promises to watch its teeth.", "Authority is a poor substitute for somebody choosing to trust you.", "Put a plate out anyway. It has been a very long morning."], ["Then I will sign the receipt and walk in beside you.", "Let the witnesses disagree. We can still listen carefully.", "I have written it down. This time the record stays outside the Archive.", "Unplug the old verdict. Let them say it aloud if they still believe it.", "You were trying to help. You also hurt them. Both things can be true.", "Then start now. Tell us what happened, and let us remember.", "I am keeping that sentence for the next time somebody gives me a fuse.", "We can carry coats. We can build shelters. We do not need a perfect forecast.", "That answer is harder than a promise. I think it is the honest one.", "The door is open. We can talk about the verdict outside."], ["I will draw the street in myself. Make the line wide enough for everyone.", "I have your signal. Take your time with the bend.", "Then we stand at the gate and welcome people. We do not close it.", "It was a very convincing explosion. Gently has improved a lot.", "I will read it aloud for the people who cannot reach the screen.", "A window can be a choice too. Ask which way they want it to face.", "I can hear the different voices. None of them is alone anymore.", "Then we will leave a lamp in every gap they cross.", "It is rough out there. I still want to see it.", "Let it hesitate. We can wait while it learns something new."], ["Leave space after the old names. The map is not finished.", "Then we can put an end on it now. Not on the helping. On the emergency.", "The pressure is falling. Everyone keep your own relay steady.", "Tell them there is breakfast. We are trying to make that a tradition.", "A safe failure is still a way to keep a promise.", "Make one extra. Somebody always arrives later than we expect.", "You can rest without knowing every possible ending. We will keep watch.", "Every one of them brought something. A lamp. A tool. A way to help.", "I want to stay. I want the people who leave to know they can come back.", "There is no last shore. Only the next one."]];
 const missions=rows.map((s,i)=>{
  const act=Math.floor(i/10),map=makeMap(i,s),base={...s,reply:reactions[act][i%10],replySpeaker:s.crew.find(r=>r!==s.speaker)||'Sol',...map,index:i,act,place:String(i+1).padStart(3,'0')+' / '+acts[act].region,objective:goals[s.goal],count:s.goal==='hold'?2:s.goal==='survive'||s.goal==='protect'?3+(i%3):s.goal==='evacuate'?Math.min(2,s.crew.length):undefined,dialogue:s.line,tip:'Right-click or hold any tile for its complete rules. Use terrain, cover and the crew’s different abilities together.',debrief:i===99?'The rain arrives without permission. A hundred relays answer, each in a different voice. The old Heart rests. Sol opens a window. Somewhere beyond the bow, a gull turns toward a shore no map has named.':'The route opens. '+acts[act].summary};
  if(i<6){const old=OPENING_MAPS[i];Object.assign(base,{width:7,height:7,shape:'opening',voids:[],tiles:old.tiles,objects:old.objects,allies:old.allies,enemies:old.enemies,flows:{},dirs:{},objective:old.objective,count:old.count||base.count});if(old.boss)base.boss=old.boss;for(const[x,y,t]of base.tiles)if(t==='water')base.flows[x+','+y]=[1,0];for(const[x,y,o]of base.objects)if(o==='fan')base.dirs[x+','+y]=i%4;}
  if(s.goal==='boss'&&!base.boss){base.boss=base.enemies[0]||[Math.floor(base.width/2),1];base.bossRole=base.enemyTypes[0];}
  // These support-led encounters use flank routes, rather than a command pad
  // directly under a guard that the crew has no way to damage.
  if([17,28,39,49].includes(i)){
   base.tiles=base.tiles.filter(p=>p[2]!=='goal');
   const targets=i===17?[[1,3],[4,2]]:i===28?[[5,3]]:i===39?[[4,1]]:[[2,1]];
   for(const[x,y]of targets){base.objects=base.objects.filter(p=>p[0]!==x||p[1]!==y);base.tiles=base.tiles.filter(p=>p[0]!==x||p[1]!==y);base.tiles.push([x,y,'goal']);delete base.flows[x+','+y];}
   base.pads=targets;
  }
  base.eventRound=s.event==='rupture'?3:2;
  return base;
 });
 return {acts,missions,goals,shapes};
})();
if(typeof module!=='undefined')module.exports=SAGA;
