describe("exercise_1_suite", function () {
  describe("anObject", function () {
    it("is an object", function () {
      expect(anObject).is.a("object");
    });
    it("has property x set to 5", function () {
      expect(anObject).to.include.keys("x");
      expect(anObject.x).equal(5);
    });
  });

  describe("anotherObject", function () {
    it("is an object", function () {
      expect(anotherObject).is.a("object");
    });
    it("has property x set to 5", function () {
      expect(anotherObject).to.include.keys("x");
      expect(anotherObject.x).equal(5);
    });
    it("has property y set to 10", function () {
      expect(anotherObject).to.include.keys("y");
      expect(anotherObject.y).equal(10);
    });
  });
});

describe("exercise_4_suite", function () {
  describe("binaryTree", function () {
    it("works correctly", function () {
      expect(binaryTree(1)).to.deep.equal({
        data: 1,
        left: undefined,
        right: undefined,
      });
      expect(
        binaryTree(1, binaryTree(2), binaryTree(3, binaryTree(4))),
      ).to.deep.equal({
        data: 1,
        left: { data: 2, left: undefined, right: undefined },
        right: {
          data: 3,
          left: { data: 4, left: undefined, right: undefined },
          right: undefined,
        },
      });
    });
  });
});

describe("exercise_5_suite", function () {
  describe("naryTree", function () {
    it("works correctly", function () {
      expect(naryTree(1)).to.deep.equal({ data: 1, children: [] });
      expect(naryTree(1, [])).to.deep.equal({ data: 1, children: [] });
      console.log(naryTree(1, [naryTree(2), naryTree(3, [naryTree(4)])]));
      expect(
        naryTree(1, [naryTree(2), naryTree(3, [naryTree(4)])]),
      ).to.deep.equal({
        data: 1,
        children: [
          { data: 2, children: [] },
          { data: 3, children: [{ data: 4, children: [] }] },
        ],
      });
    });
  });
});

describe("exercise_6_suite", function () {
  describe("Base cases", function () {
    it("null", function () {
      expect(prettifyJson(null)).is.equal("null");
    });
    it("string", function () {
      expect(prettifyJson("hello")).is.equal("hello");
    });
    it("number", function () {
      expect(prettifyJson(0)).is.equal("0");
      expect(prettifyJson(-1)).is.equal("-1");
      expect(prettifyJson(123)).is.equal("123");
    });
    it("boolean", function () {
      expect(prettifyJson(false)).is.equal("false");
      expect(prettifyJson(true)).is.equal("true");
    });
  });
  const strip = (s) => s.replace(/\s/g, "");
  describe("Arrays", function () {
    it("simple array", function () {
      expect(strip(prettifyJson([1, 2, 3, 4]))).is.equal("[1,2,3,4]");
    });
  });
  describe("Objects", function () {
    it("simple object", function () {
      expect(strip(prettifyJson({ a: 1 }))).is.equal("{a:1}");
    });
    it("complex object", function () {
      const str = `{
        unit: FIT2102,
        year: 2021,
        semester: S2,
        active: true,
        assessments: {
          week1: null,
          week2: Tutorial 1 Exercise,
          week3: Tutorial 2 Exercise
        },
        languages: [
          Javascript,
          Typescript,
          Haskell,
          Minizinc
        ]
      }`;
      expect(strip(prettifyJson(json))).equal(strip(str));
    });
  });
});
