from scripts.generate_manifest import build_manifest


def test_manifest_uses_expected_fields() -> None:
    manifest = build_manifest()

    assert isinstance(manifest, list)
    assert manifest, "Corpus manifest should not be empty when corpus PDFs are present."

    first = manifest[0]
    assert "book_title" in first
    assert "source_file" in first
    assert "path" in first
