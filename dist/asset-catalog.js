'use strict';
const ART_CATALOG={
  "version": "simple-raster-2",
  "size": 80,
  "roles": {
    "vanguard": {
      "src": "assets/art/roles/vanguard.png"
    },
    "ranger": {
      "src": "assets/art/roles/ranger.png"
    },
    "gardener": {
      "src": "assets/art/roles/gardener.png"
    },
    "engineer": {
      "src": "assets/art/roles/engineer.png"
    },
    "tidecaller": {
      "src": "assets/art/roles/tidecaller.png"
    },
    "archer": {
      "src": "assets/art/roles/archer.png"
    },
    "medic": {
      "src": "assets/art/roles/medic.png"
    },
    "carrier": {
      "src": "assets/art/roles/carrier.png"
    },
    "mawkeeper": {
      "src": "assets/art/roles/mawkeeper.png"
    },
    "vinekeeper": {
      "src": "assets/art/roles/vinekeeper.png"
    },
    "shaman": {
      "src": "assets/art/roles/shaman.png"
    },
    "blight": {
      "src": "assets/art/roles/blight.png"
    },
    "bulldozer": {
      "src": "assets/art/roles/bulldozer.png"
    },
    "witch": {
      "src": "assets/art/roles/witch.png"
    },
    "astronomer": {
      "src": "assets/art/roles/astronomer.png"
    },
    "digger": {
      "src": "assets/art/roles/digger.png"
    },
    "geomancer": {
      "src": "assets/art/roles/geomancer.png"
    },
    "sapper": {
      "src": "assets/art/roles/sapper.png"
    },
    "mirror": {
      "src": "assets/art/roles/mirror.png"
    },
    "blink": {
      "src": "assets/art/roles/blink.png"
    },
    "ferryman": {
      "src": "assets/art/roles/ferryman.png"
    },
    "builder": {
      "src": "assets/art/roles/builder.png"
    },
    "alchemist": {
      "src": "assets/art/roles/alchemist.png"
    },
    "firestarter": {
      "src": "assets/art/roles/firestarter.png"
    },
    "warden": {
      "src": "assets/art/roles/warden.png"
    },
    "herder": {
      "src": "assets/art/roles/herder.png"
    },
    "gust": {
      "src": "assets/art/roles/gust.png"
    },
    "magnet": {
      "src": "assets/art/roles/magnet.png"
    },
    "courier": {
      "src": "assets/art/roles/courier.png"
    },
    "anchorite": {
      "src": "assets/art/roles/anchorite.png"
    },
    "tinkerer": {
      "src": "assets/art/roles/tinkerer.png"
    },
    "conductor": {
      "src": "assets/art/roles/conductor.png"
    },
    "weaver": {
      "src": "assets/art/roles/weaver.png"
    },
    "siren": {
      "src": "assets/art/roles/siren.png"
    },
    "icewright": {
      "src": "assets/art/roles/icewright.png"
    },
    "beekeeper": {
      "src": "assets/art/roles/beekeeper.png"
    },
    "demolition": {
      "src": "assets/art/roles/demolition.png"
    },
    "recaller": {
      "src": "assets/art/roles/recaller.png"
    },
    "scout": {
      "src": "assets/art/roles/scout.png"
    },
    "liberator": {
      "src": "assets/art/roles/liberator.png"
    },
    "harvester": {
      "src": "assets/art/roles/harvester.png"
    },
    "plumber": {
      "src": "assets/art/roles/plumber.png"
    },
    "rainmaker": {
      "src": "assets/art/roles/rainmaker.png"
    },
    "firefighter": {
      "src": "assets/art/roles/firefighter.png"
    },
    "mason": {
      "src": "assets/art/roles/mason.png"
    },
    "lantern": {
      "src": "assets/art/roles/lantern.png"
    },
    "spore": {
      "src": "assets/art/roles/spore.png"
    },
    "puppeteer": {
      "src": "assets/art/roles/puppeteer.png"
    },
    "rigger": {
      "src": "assets/art/roles/rigger.png"
    },
    "bombardier": {
      "src": "assets/art/roles/bombardier.png"
    }
  },
  "enemies": {
    "sentinel": {
      "src": "assets/art/enemies/sentinel.png"
    },
    "brute": {
      "src": "assets/art/enemies/brute.png"
    },
    "gunner": {
      "src": "assets/art/enemies/gunner.png"
    },
    "mortar": {
      "src": "assets/art/enemies/mortar.png"
    },
    "webber": {
      "src": "assets/art/enemies/webber.png"
    },
    "arsonist": {
      "src": "assets/art/enemies/arsonist.png"
    },
    "sower": {
      "src": "assets/art/enemies/sower.png"
    },
    "sapper": {
      "src": "assets/art/enemies/sapper.png"
    },
    "leech": {
      "src": "assets/art/enemies/leech.png"
    },
    "healer": {
      "src": "assets/art/enemies/healer.png"
    },
    "rammer": {
      "src": "assets/art/enemies/rammer.png"
    },
    "mesmer": {
      "src": "assets/art/enemies/mesmer.png"
    },
    "warden": {
      "src": "assets/art/enemies/warden.png"
    },
    "drone": {
      "src": "assets/art/enemies/drone.png"
    },
    "foundry": {
      "src": "assets/art/enemies/foundry.png"
    },
    "saboteur": {
      "src": "assets/art/enemies/saboteur.png"
    },
    "bellkeeper": {
      "src": "assets/art/enemies/bellkeeper.png"
    },
    "frost": {
      "src": "assets/art/enemies/frost.png"
    },
    "heart": {
      "src": "assets/art/enemies/heart.png"
    },
    "sovereign": {
      "src": "assets/art/enemies/sovereign.png"
    }
  },
  "terrain": {
    "ground": {
      "src": "assets/art/terrain/ground.png",
      "variants": [
        "assets/art/terrain/ground-1.png",
        "assets/art/terrain/ground-2.png",
        "assets/art/terrain/ground-3.png"
      ]
    },
    "water": {
      "src": "assets/art/terrain/water.png",
      "variants": [
        "assets/art/terrain/water-1.png",
        "assets/art/terrain/water-2.png",
        "assets/art/terrain/water-3.png"
      ]
    },
    "ice": {
      "src": "assets/art/terrain/ice.png"
    },
    "fire": {
      "src": "assets/art/terrain/fire.png"
    },
    "goal": {
      "src": "assets/art/terrain/goal.png"
    },
    "mud": {
      "src": "assets/art/terrain/mud.png"
    },
    "poison": {
      "src": "assets/art/terrain/poison.png"
    },
    "conveyor": {
      "src": "assets/art/terrain/conveyor.png"
    },
    "cracked": {
      "src": "assets/art/terrain/cracked.png"
    },
    "pit": {
      "src": "assets/art/terrain/pit.png"
    },
    "lava": {
      "src": "assets/art/terrain/lava.png"
    },
    "thorns": {
      "src": "assets/art/terrain/thorns.png"
    },
    "grass": {
      "src": "assets/art/terrain/grass.png",
      "variants": [
        "assets/art/terrain/grass-1.png",
        "assets/art/terrain/grass-2.png",
        "assets/art/terrain/grass-3.png"
      ]
    },
    "smoke": {
      "src": "assets/art/terrain/smoke.png"
    },
    "mist": {
      "src": "assets/art/terrain/mist.png"
    },
    "charged": {
      "src": "assets/art/terrain/charged.png"
    },
    "quicksand": {
      "src": "assets/art/terrain/quicksand.png"
    },
    "moss": {
      "src": "assets/art/terrain/moss.png"
    },
    "runway": {
      "src": "assets/art/terrain/runway.png"
    },
    "snow": {
      "src": "assets/art/terrain/snow.png"
    },
    "springwater": {
      "src": "assets/art/terrain/springwater.png"
    }
  },
  "objects": {
    "wall": {
      "src": "assets/art/objects/wall.png"
    },
    "tree": {
      "src": "assets/art/objects/tree.png"
    },
    "column": {
      "src": "assets/art/objects/column.png"
    },
    "crate": {
      "src": "assets/art/objects/crate.png"
    },
    "seed": {
      "src": "assets/art/objects/seed.png"
    },
    "lever": {
      "src": "assets/art/objects/lever.png"
    },
    "gate": {
      "src": "assets/art/objects/gate.png"
    },
    "bomb": {
      "src": "assets/art/objects/bomb.png"
    },
    "fan": {
      "src": "assets/art/objects/fan.png"
    },
    "barrel": {
      "src": "assets/art/objects/barrel.png"
    },
    "boulder": {
      "src": "assets/art/objects/boulder.png"
    },
    "mirror": {
      "src": "assets/art/objects/mirror.png"
    },
    "spring": {
      "src": "assets/art/objects/spring.png"
    },
    "portal": {
      "src": "assets/art/objects/portal.png"
    },
    "bridge": {
      "src": "assets/art/objects/bridge.png"
    },
    "plate": {
      "src": "assets/art/objects/plate.png"
    },
    "spikes": {
      "src": "assets/art/objects/spikes.png"
    },
    "beacon": {
      "src": "assets/art/objects/beacon.png"
    },
    "vine": {
      "src": "assets/art/objects/vine.png"
    },
    "maw": {
      "src": "assets/art/objects/maw.png"
    },
    "haste": {
      "src": "assets/art/objects/haste.png"
    },
    "blight": {
      "src": "assets/art/objects/blight.png"
    },
    "pump": {
      "src": "assets/art/objects/pump.png"
    },
    "generator": {
      "src": "assets/art/objects/generator.png"
    },
    "switch": {
      "src": "assets/art/objects/switch.png"
    },
    "nest": {
      "src": "assets/art/objects/nest.png"
    },
    "cage": {
      "src": "assets/art/objects/cage.png"
    },
    "supply": {
      "src": "assets/art/objects/supply.png"
    },
    "relic": {
      "src": "assets/art/objects/relic.png"
    },
    "console": {
      "src": "assets/art/objects/console.png"
    },
    "cart": {
      "src": "assets/art/objects/cart.png"
    },
    "anchor": {
      "src": "assets/art/objects/anchor.png"
    },
    "emitter": {
      "src": "assets/art/objects/emitter.png"
    },
    "glass": {
      "src": "assets/art/objects/glass.png"
    },
    "oil": {
      "src": "assets/art/objects/oil.png"
    },
    "bell": {
      "src": "assets/art/objects/bell.png"
    },
    "rod": {
      "src": "assets/art/objects/rod.png"
    },
    "drain": {
      "src": "assets/art/objects/drain.png"
    },
    "sign": {
      "src": "assets/art/objects/sign.png"
    }
  },
  "companions": {
    "worker-drone": {
      "src": "assets/art/companions/worker-drone.png"
    }
  }
};
